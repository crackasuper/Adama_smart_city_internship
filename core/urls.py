from django.urls import path
from .views import SignUpView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', SignUpView.as_view(), name= 'signup'),
]
