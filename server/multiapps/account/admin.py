from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import User, Transaction
from home.admin_inline import ExpenseGroupInline
from account.admin_inline import TransactionInline
# Register your model admin here.


@admin.register(User)
class UserAdmin(UserAdmin):
  inlines = [ExpenseGroupInline, TransactionInline.new_klass(fk_name='payer')]
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
  list_display = ('payer', 'borrower', 'group_through', 'amount', 'return_status')
  search_fields = ('payer', 'borrower', 'group_through')

