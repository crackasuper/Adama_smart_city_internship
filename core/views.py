from django.shortcuts import render, redirect
from shop.models import *
from .models import *
from django.contrib.auth.decorators import login_required
from carts.views import *
from carts.models import *
from .forms import SignUpForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView
from django.contrib.auth.models import User

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

class CustomLogoutView(LogoutView):
    template_name = 'registration/logged_out.html'

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
