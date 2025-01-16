from django.urls import path
from . import views
from .auth_views import TherapistLoginView, TherapistLogoutView, TherapistRegistrationView

app_name = 'therapy'

urlpatterns = [
    path('', views.daily_input, name='daily_input'),
    path('results/', views.results, name='results'),
    path('login/', TherapistLoginView.as_view(), name='login'),
    path('logout/', TherapistLogoutView.as_view(), name='logout'),
    path('register/', TherapistRegistrationView.as_view(), name='register'),
    path('profile/', views.profile, name='profile'),
    path('about/', views.about, name='about'),
    path('home/', views.home, name='home'),
]

