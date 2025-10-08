from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Account


class AccountCreationForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ["username", "full_name", "phone", "password1", "password2"]


class AccountAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Placeholders RTL-friendly
        self.fields["username"].widget.attrs.update({
            "placeholder": "اسم المستخدم / البريد الإلكتروني"
        })
        self.fields["password"].widget.attrs.update({
            "placeholder": "كلمة المرور"
        })
    class Meta:
        model = Account
        fields = ["username", "password"]
