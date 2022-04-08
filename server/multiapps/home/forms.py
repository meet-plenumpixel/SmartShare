from django import forms
from crispy_forms.helper import FormHelper

from home.models import Expense

# Create your forms here.

class ExpenseForm(forms.ModelForm):

  class Meta:
    model = Expense
    fields = ('title', 'detail', 'amount', 'group')

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.form_tag = False
