from django.contrib import admin
from home.models import Expense, ExpenseGroup
from account.inlines.inline_admin import TransactionInlineAdmin
# Register your model admin here.


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):

  list_display = ('title', 'group', 'amount')
  search_fields = ('title',)


@admin.register(ExpenseGroup)
class ExpenseGroupAdmin(admin.ModelAdmin):
  inlines = [TransactionInlineAdmin.new_klass(fk_name='group_through')]
  list_display = ('name', 'owner')
  search_fields = ('name', 'owner')
  filter_horizontal = ('members',)
  exclude = None

 