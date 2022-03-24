# from django import forms
from account.models import UserAccount
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class UserRegisterForm(UserCreationForm):
  template_name_div = 'div.html'
  class Meta:
    model = UserAccount
    fields = UserCreationForm.Meta.fields + ('email',)

  def as_div(self, *args, **kwargs):
    """Render as <p> elements."""
    return self.render(self.template_name_div, *args, **kwargs)

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
