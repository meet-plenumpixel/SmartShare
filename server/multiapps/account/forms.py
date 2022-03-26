from django import forms
from account.models import UserAccount
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# from crispy_forms.helper import FormHelper

# Create your forms here.

class UserRegisterForm(UserCreationForm):
 
  class Meta:
    model = UserAccount
    fields = UserCreationForm.Meta.fields + ('email',)


class UserUpdateForm(forms.ModelForm):
  class Meta(UserChangeForm.Meta):
    model = UserAccount
    fields = ('username','first_name', 'last_name', 'email', 'balance', 'image')

