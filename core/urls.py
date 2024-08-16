
from django.urls import path
from .views import  CustomPasswordResetView, SignUpView
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name='home'),
    
    path('signup/', SignUpView.as_view(), name= 'signup'),
    path('logout/', views.logout_user, name='logout'),
    path('dasboard/',views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),

   # path('accounts/password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),

    
   
]
