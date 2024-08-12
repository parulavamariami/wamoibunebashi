from django.contrib.auth.forms import UserCreationForm
from .models import User, Service
from django.forms import ModelForm
from django import forms


class MyUserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = '__all__'

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'username', 'email', 'bio', 'services']


class ContactForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'სახელი'
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email'
        })
    )
    subject = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'სათაური'
        })
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'შინაარსი',
            'rows': 4
        })
    )