
from django.urls import include, path
from .views import  CustomPasswordResetView, SignUpView
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView


urlpatterns = [
    path('', views.home, name='home'),
    
    path('signup/', SignUpView.as_view(), name= 'signup'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('contact_us/',views.contact_us, name='contact_us'),
    path('about_us/', views.about_us, name= 'about_us'),
 
   
]
