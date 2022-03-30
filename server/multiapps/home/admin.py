from django.contrib import admin
from home.models import Expense, ExpenseGroup

# Register your models here.


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):

  list_display = ('title', 'amount', 'pay_by')
  search_fields = ('title', 'pay_by')
  filter_horizontal= ('contributor',)


@admin.register(ExpenseGroup)
class ExpenseGroupAdmin(admin.ModelAdmin):

  list_display = ('name', 'owner')
  search_fields = ('name', 'owner')
  filter_horizontal= ('members',)
