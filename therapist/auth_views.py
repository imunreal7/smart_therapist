from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import RegistrationForm

class TherapistLoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('therapy:daily_input')

class TherapistLogoutView(LogoutView):
    next_page = reverse_lazy('therapy:login')

class TherapistRegistrationView(CreateView):
    template_name = 'register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('therapy:login')

