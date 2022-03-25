from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import UserAccount, UserExpense, UserGroup
# Register your models here.


@admin.register(UserAccount)
class UserAccountAdmin(UserAdmin):
  search_fields = ('username','email')

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fieldsets[1][1]['fields'] += ("balance", "image")


@admin.register(UserExpense)
class UserExpenseAdmin(admin.ModelAdmin):

  list_display = ('title', 'amount', 'pay_by')
  search_fields = ('title', 'pay_by')
  filter_horizontal= ('contributor',)


@admin.register(UserGroup)
class UserGroupAdmin(admin.ModelAdmin):

  list_display = ('name', 'owner')
  search_fields = ('name', 'owner')
  filter_horizontal= ('members',)
