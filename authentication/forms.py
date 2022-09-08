from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='Usuario', max_length=60)
    password = forms.CharField(label='Contraseña', max_length=60, widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    first_name = forms.CharField(label='Nombre', max_length=30)
    last_name = forms.CharField(label='Apellidos', max_length=60, required=False)
    email = forms.CharField(max_length=90, required=False)
    username = forms.CharField(label='Usuario', max_length=60)
    password = forms.CharField(label='Contraseña', max_length=60, widget=forms.PasswordInput)