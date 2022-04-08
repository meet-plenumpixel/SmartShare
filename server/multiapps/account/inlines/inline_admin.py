from django.contrib import admin
from account.models import UserGroup, LoanHistory
# Register your inline model admin here.


class UserGroupInlineAdmin(admin.TabularInline):
  model = UserGroup
  extra = 1
  # raw_id_fields = ('members',)
  # filter_horizontal = ('members',)


class LoanHistoryInlineAdmin(admin.TabularInline):
  model = LoanHistory
  extra = 1

  @classmethod
  def new_klass(cls, fk_name=None):
    return type('LoanHistoryInline', (cls,), {'fk_name':fk_name})

