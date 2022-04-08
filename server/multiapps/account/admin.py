from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from account.inlines.inline_admin import UserGroupInlineAdmin, LoanHistoryInlineAdmin

from account.models import User, UserGroup, LoanHistory
# Register your model admin here.


@admin.register(User)
class UserAdmin(UserAdmin):
  inlines = [UserGroupInlineAdmin, LoanHistoryInlineAdmin.new_klass(fk_name='borrower')]
  list_display = ('username', 'first_name', 'last_name', 'email', 'total_balance', 'total_credit', 'total_debit', 'is_staff')
  search_fields = ('username','email')
  # raw_id_fields = ('exp_groups',)
  # filter_horizontal = ('exp_groups',)

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fieldsets[1][1]['fields'] += ('image',)
    self.fieldsets = self.fieldsets[:2] + (
      (_('Account'), {'fields': ('total_balance', 'total_credit', 'total_debit')}),
    ) + self.fieldsets[2:]


@admin.register(UserGroup)
class UserGroupAdmin(admin.ModelAdmin):
  inlines = [LoanHistoryInlineAdmin.new_klass(fk_name='group_through')]
  list_display = ('name', 'owner')
  search_fields = ('name', 'owner')
  filter_horizontal = ('members',)
  exclude = None


@admin.register(LoanHistory)
class LoanHistoryAdmin(admin.ModelAdmin):
  # Problem: show owner(admin) in admin change_list view (list_display)
  list_display = ('borrower', 'group_through', 'have_to_pay')   #, 'group_through__owner')
  list_select_related = ('group_through__owner', )
  list_filter = ('group_through',)
  search_fields = ('borrower', 'group_through')
