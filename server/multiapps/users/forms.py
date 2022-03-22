from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users.models import ProfileModel


class UserRegisterForm(UserCreationForm):
  email = forms.EmailField()

  class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2']


class ProfileCreationForm(forms.ModelForm):

  class Meta:
    model = ProfileModel
    fields = ['user', 'image', 'phone_number']
  