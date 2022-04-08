from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import User, Transaction

from account.inlines.inline_admin import TransactionInlineAdmin
from home.inlines.inline_admin import ExpenseGroupInlineAdmin

# Register your model admin here.


@admin.register(User)
class UserAdmin(UserAdmin):
  inlines = [ExpenseGroupInlineAdmin, TransactionInlineAdmin.new_klass(fk_name='borrower')]
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


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
  # Problem: show owner(admin) in admin change_list view (list_display)
  list_display = ('borrower', 'group_through', 'amount')   #, 'group_through__owner')
  list_select_related = ('group_through__owner', )
  search_fields = ('borrower', 'group_through')

