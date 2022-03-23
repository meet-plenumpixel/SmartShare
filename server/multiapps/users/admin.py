from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as User_Admin
from users.models import User

# Register your models here.

@admin.register(User)
class UserAdmin(User_Admin):
  model = User

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fieldsets[1][1]['fields'] += ("phone_number", "image")
  