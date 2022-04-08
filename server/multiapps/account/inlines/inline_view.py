from extra_views import InlineFormSetFactory
from account.models import UserGroup, LoanHistory

class UserGroupInlineFormSet(InlineFormSetFactory):
  model = UserGroup
  fields = ('name', 'owner')
  factory_kwargs = {
    # 'fk_name': 'payer',
    'extra': 1
  }


class LoanHistoryInlineFormSet(InlineFormSetFactory):
  model = LoanHistory
  fields = ('borrower', 'group_through', 'amount')
  factory_kwargs = {
    'fk_name': 'borrower',
    'extra': 1
  }

