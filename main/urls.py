
from django.urls import path
from .import views
app_name="main"
urlpatterns = [
    
    path('', views.base,name="base"),
   
    path('about/', views.about,name="about"),
    path('register/', views.register,name="register"),
    path('logout/', views.logout_request,name="logout"),
    path('login/', views.login_request,name="login"),
    path('profile/', views.profile,name="profile"),
    path('result', views.result,name="result"),

]
