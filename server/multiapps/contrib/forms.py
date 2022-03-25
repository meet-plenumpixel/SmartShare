from django.contrib.auth.password_validation import get_default_password_validators
from utils.validation import help_text_html

class BootstrapAuthForm:
  template_name_login = 'bootstrap/forms/auth_form.html'

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    if(field:=self.fields.get('password1')):
      field.help_text = help_text_html(
        get_default_password_validators(),
        self.help_text_wrapper
      )

  def as_auth(self, *args, **kwargs):
    """Render form for login form"""
    return self.render(self.template_name_login, *args, **kwargs)

