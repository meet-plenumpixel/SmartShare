from django.contrib import admin
from home.models import Expense, ExpenseGroup
from account.admin_inline import TransactionInline
# Register your model admin here.


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):

  list_display = ('title', 'group', 'amount')
  search_fields = ('title',)


@admin.register(ExpenseGroup)
class ExpenseGroupAdmin(admin.ModelAdmin):
  inlines = [TransactionInline.new_klass(fk_name='group_through')]
  list_display = ('name',)
  search_fields = ('name',)
  filter_horizontal = ('members',)

 