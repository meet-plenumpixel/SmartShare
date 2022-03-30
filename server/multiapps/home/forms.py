from django import forms
from home.models import Expense, ExpenseGroup

# Create your forms here.


class ExpenseGroupForm(forms.ModelForm):

  class Meta:
    model = ExpenseGroup
    fields = ('name', 'owner', 'members')
    widgets = {
      'owner': forms.HiddenInput()
    }

  
  def __init__(self, *args, **kwargs):
    user = kwargs.pop('user', None)
    kwargs['initial'].update({'owner': user})

    super().__init__(*args, **kwargs)

    if user:
      self.fields['members'].queryset = self.fields['members'].queryset.exclude(id=user.pk)
