from django import forms
from home import models as home_model
from contrib.widgets import CheckboxSelectMultipleWidget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Field


class ExpenseGroupForm(forms.ModelForm):

  class Meta:
    model = home_model.ExpenseGroup
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
  
