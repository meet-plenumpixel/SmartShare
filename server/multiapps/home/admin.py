from django.contrib import admin
from home.models import Expense

# Register your model admin here.

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):

  list_display = ('title', 'group', 'amount')
  search_fields = ('title',)

