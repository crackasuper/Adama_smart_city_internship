from django.urls import path
from .views import CustomLogoutView, SignUpView
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    #path('login/', LoginView.as_view(template_name = 'login.html'), name= 'login'),
    path('signup/', SignUpView.as_view(), name= 'signup'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]
