from django import forms
from django.conf import settings
from . models import User
from django.contrib.auth.forms import UserCreationForm

# user registration form
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'class': 'input100',
        'name': 'email'
    }))
    password1 = forms.CharField(widget=forms.TextInput(attrs={
        'name': 'password1',
        'class': 'input100',
        'type': 'password'
    }))
    password2 = forms.CharField(widget=forms.TextInput(attrs={
        'name': 'password2',
        'class': 'input100',
        'type': 'password'
    }))

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']