from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import UserAccount
# Register your models here.


@admin.register(UserAccount)
class UserAccountAdmin(UserAdmin):
  list_display = ('username', 'first_name', 'last_name', 'email', 'balance', 'is_staff')
  search_fields = ('username','email')

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fieldsets[1][1]['fields'] += ("balance", "image")
