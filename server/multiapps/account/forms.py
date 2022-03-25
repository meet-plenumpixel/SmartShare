# from django import forms
from account.models import UserAccount
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from contrib.forms import BootstrapAuthForm


class UserRegisterForm(BootstrapAuthForm, UserCreationForm):
  help_text_wrapper = {
    'element': ('div', {'class':'form-text'}),
    'grouped': ('div', {'class':'helptexts'})
  }
  

  # def render(self, *args, **kwargs):
  #   print(args)
  #   print(kwargs)
  #   print()
  #   temp = super().render(*args, **kwargs)
  #   print(temp)
  #   return temp
    
  class Meta:
    model = UserAccount
    fields = UserCreationForm.Meta.fields + ('email',)

  # def clean(self):
  #   super().clean()
  #   username = self.cleaned_data['username']
  #   if self.model.objects.exclude(pk=self.instance.pk).filter(username=username).exists():
  #       raise forms.ValidationError(f'Username "{username}" is already in use.')
  #   return username

class UserLoginForm(AuthenticationForm):

  def clean(self):
    cleaned_data = super().clean()
    print(cleaned_data)
    return cleaned_data
