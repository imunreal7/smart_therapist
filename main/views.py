from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from main.utils import classify_dataset
from .forms import myForm
# Create your views here.
def base(request):
	return render(request=request,template_name="main/base.html",
					context={"Users": User.objects.all})


def about(request):
	return render(request=request,template_name="main/about.html")
	

def homepage(request):
	return HttpResponse("Homepage")


def register(request):
	if request.method =="POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			stuser = form.save()
			username = form.cleaned_data.get('username')
			messages.success(request,f"New Account is succesfully created: {username}")
			login(request, stuser)
			messages.info(request,f"You are now logged in as:{username}")
			return redirect("main:base")

	form = UserCreationForm
	return render(request,"main/register.html",context={"form":form})

def profile(request):
	return render(request=request,template_name="main/profile.html")

'''def result(request,data):

	inputData=request.cleaned_data.get('data')
	result=classify_dataset(inputData)
	return render(request,"main/result.html",{"result":result} ) '''

'''def result(request):
	if request.method == 'POST':  # data sent by user
		form = myForm(request.POST)
		if form.is_valid():
			inputData=request.cleaned_data.get('formData')
			result=classify_dataset(inputData)
			form.save()  # this will save Car info to database
			return HttpResponse('data is added to database')
		else:
		  # display empty form
		form = myForm()
	return render(request, 'result.html', {'result': result})'''
def result(request):
	if request.method == 'POST': 
		form = myForm(request.POST)
		print(form)
		if form.is_valid():
			text = form.cleaned_data['data']
			text.save()
		else:
			text="wrong"
		res = classify_dataset(text)
		context = {
        'form': form,
        'text': text,
    }

		args = {'form': form , 'text': text }
	else:
		form = myForm()
	return render(request,'main/result.html',context)


	


def logout_request(request):
	logout(request)
	messages.info(request,"Succesfully logged out !")
	return redirect("main:base")

def login_request(request):
	if request.method =="POST":
		form =AuthenticationForm(request,data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username,password=password)
			if user is not None:
				login(request,user)
				messages.info(request,f"You are now logged in as:{username}")
				return redirect("main:base")
				
			else:
				messages.error(request,"Invalid username or password")
		
	form =AuthenticationForm()
	return render(request,"main/login.html",{"form" : form})
