from django.contrib.auth.models import User
from django.forms import forms
from .models import *
from django import forms


class RegistrationForm(forms.Form):
    ROLES = (
        ('patient', 'Пациент'),
        ('doctor', 'Врач'),
    )

    username = forms.CharField(label='Имя пользователя', max_length=100)
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    role = forms.ChoiceField(label='Роль', choices=ROLES)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Пользователь с таким именем уже существует')
        return username
