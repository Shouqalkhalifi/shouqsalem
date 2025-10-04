from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Account


class AccountCreationForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ["username", "full_name", "phone", "password1", "password2"]


class AccountAuthenticationForm(AuthenticationForm):
    class Meta:
        model = Account
        fields = ["username", "password"]
