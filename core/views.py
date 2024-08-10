from django.shortcuts import render, redirect
from shop.models import *
from .models import *
from django.contrib.auth.decorators import login_required
from carts.views import *
from carts.models import *
from .forms import SignUpForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin

class CustomLoginView(LoginView):
    
    template_name = 'registration/login.html'
    next_page = 'home'
    

def LoginView(request):
    form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


class CustomLogoutView(LoginRequiredMixin, LogoutView):

    
    template_name = 'registration/logged_out.html'
    next_page = reverse_lazy('home')

class CustomPasswordResetView(PasswordResetView):
    template_name = 'registration/password_reset.html'
    email_template_name = 'registration/password_reset_email.html'
    success_url = reverse_lazy('password_reset_done')

class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.success_url)

def home(request):
    products = Product.objects.all()
    cat = Category.objects.all()
    return render(request, 'index.html', {'products': products, 'cat':cat})





# Create your views here.
