from django.contrib.auth.models import User
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='Usuario', max_length=60)
    password = forms.CharField(label='Contraseña', max_length=60, widget=forms.PasswordInput)

class RegisterForm(forms.ModelForm):
    username = forms.CharField(label='Usuario', max_length=60)
    password = forms.CharField(label='Contraseña', max_length=60, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "username", "password")