from account.models import UserAccount
from django.contrib.auth.forms import UserCreationForm

# Create your forms here.

class UserRegisterForm(UserCreationForm):
 
  class Meta:
    model = UserAccount
    fields = UserCreationForm.Meta.fields + ('email',)
