from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Field
from contrib.widgets import CheckboxSelectMultipleWidget
from account.models import User, UserGroup, LoanHistory


# Create your forms here.


class LoanHistoryForm(forms.ModelForm):

  class Meta:
    model = LoanHistory
    fields = ('borrower', 'group_through', 'have_to_pay')

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.form_tag = False



class UserGroupForm(forms.ModelForm):

  class Meta:
    model = UserGroup
    fields = ('name', 'owner', 'members')

    widgets = {
      'members': CheckboxSelectMultipleWidget()
    }

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.form_tag = False
    # self.helper.layout = Layout(
    #   # Fieldset(
    #     # 'first arg is the legend of the fieldset',
    #     'name',
    #     'members',
    #     # Field('members', multiple="multiple")
    #   # ),
    #   # ButtonHolder(
    #   #   Submit('submit', 'Submit', css_class='button white')
    #   # )
    # )


class UserRegisterForm(UserCreationForm):
 
  class Meta:
    model = User
    fields = ('username','first_name', 'last_name', 'email')


class UserUpdateForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ('username','first_name', 'last_name', 'email', 'image')
