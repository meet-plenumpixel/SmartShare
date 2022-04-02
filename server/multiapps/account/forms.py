from django import forms
from account.models import User  #, UserGroup
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# Create your forms here.


class UserRegisterForm(UserCreationForm):
 
  class Meta:
    model = User
    fields = ('username','first_name', 'last_name', 'email')


class UserUpdateForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ('username','first_name', 'last_name', 'email', 'image')
