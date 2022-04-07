from django.contrib import admin
from home.models import ExpenseGroup
# Register your inline model admin here.


class ExpenseGroupInlineAdmin(admin.TabularInline):
  model = ExpenseGroup
  extra = 1
  # raw_id_fields = ('members',)
  # filter_horizontal = ('members',)
