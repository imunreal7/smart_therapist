from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from .models import DailyInput, UserProfile
from .forms import DailyInputForm, UserProfileForm
from textblob import TextBlob
from datetime import timedelta
from django.template.loader import render_to_string
from transformers import pipeline


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


@login_required
def daily_input(request):
    if request.method == 'POST':
        form = DailyInputForm(request.POST)
        if form.is_valid():
            daily_input = form.save(commit=False)
            daily_input.user = request.user

            # Perform emotion analysis
            emotion_analyzer = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")
            emotions = emotion_analyzer(daily_input.text)
            emotion_label = emotions[0]['label']  # Most likely emotion

            # Save the emotion to the database
            daily_input.emotion = emotion_label  # Add an `emotion` field in the model
            daily_input.save()

            # Check for consecutive negative emotions
            # print("request.user", request.user)
            check_negative_streak(request.user)

            return redirect('therapy:results')
    else:
        form = DailyInputForm()

    return render(request, 'daily_input.html', {'form': form})


def check_negative_streak(user):
    # Fetch the last three daily inputs for the user, ordered by date
    last_three_inputs = DailyInput.objects.filter(user=user).order_by('-date')[:3]
    print("last_three_inputs", last_three_inputs)
    # Define a set of negative emotions
    negative_emotions = {'Anger', 'Sadness', 'Fear', 'Disgust'}

    # Check if the last three inputs all have negative emotions
    if len(last_three_inputs) == 3 and all(input.emotion in negative_emotions for input in last_three_inputs):
        send_notification_emails(user)


@login_required
def results(request):
    date = request.GET.get('date')
    if date:
        inputs = DailyInput.objects.filter(user=request.user, date__date=date)
        average_sentiment = DailyInput.get_daily_average(request.user, date)
    else:
        inputs = DailyInput.objects.filter(user=request.user)
        average_sentiment = None

    return render(request, 'results.html', {
        'inputs': inputs,
        'average_sentiment': average_sentiment,
        'selected_date': date
    })

def send_notification_emails(user):
    try:
        # Ensure user is passed correctly
        profile = UserProfile.objects.get(user=user)
        context = {
            'user': user,  # Use user directly
        }

        # Render the email content from template
        subject = render_to_string('emails/notification_email.txt', context).split('\n')[0]
        message = render_to_string('emails/notification_email.txt', context)

        # Send email
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = []
        if profile.parent_email:
            recipient_list.append(profile.parent_email)
        if profile.doctor_email:
            recipient_list.append(profile.doctor_email)

        if recipient_list:  # Only send if recipients exist
            send_mail(subject, message, from_email, recipient_list)
    except UserProfile.DoesNotExist:
        # Log the exception or handle it gracefully
        pass


@login_required
def profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('therapy:profile')
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'profile.html', {'form': form})
