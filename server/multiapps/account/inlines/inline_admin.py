from django.contrib import admin
from account.models import Transaction
# Register your inline model admin here.


class TransactionInlineAdmin(admin.TabularInline):
  model = Transaction
  extra = 1

  @classmethod
  def new_klass(cls, fk_name=None):
    return type('TransactionInline', (cls,), {'fk_name':fk_name})

