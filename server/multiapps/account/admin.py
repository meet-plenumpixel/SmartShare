from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import UserAccount
# Register your models here.

@admin.register(UserAccount)
class UserAccountAdmin(UserAdmin):
  model = UserAccount

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fieldsets[1][1]['fields'] += ("balance", "image")
  