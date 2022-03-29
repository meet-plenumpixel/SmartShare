from django import forms
from account.models import UserAccount  #, UserGroup
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# from crispy_forms.helper import FormHelper

# Create your forms here.

class UserRegisterForm(UserCreationForm):
 
  class Meta:
    model = UserAccount
    fields = ('username','first_name', 'last_name', 'email')


class UserUpdateForm(forms.ModelForm):
  class Meta:
    model = UserAccount
    fields = ('username','first_name', 'last_name', 'email', 'balance', 'image')
    # localized_fields = ('username',)


# UserGroupFormSet = forms.modelformset_factory(
#   model=UserGroup,
#   field = ('name', 'owner')
# )


