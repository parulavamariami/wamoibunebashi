from django.contrib.auth.forms import UserCreationForm
from .models import User, Service
from django.forms import ModelForm


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