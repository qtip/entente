
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Sign-up form includes fields for username, email and passwords
class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
