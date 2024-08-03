from allauth.account.forms import SignupForm # type: ignore
from django import forms

class CustomSIgnupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    email = forms.EmailField(max_length=254, label='Email Address')
    