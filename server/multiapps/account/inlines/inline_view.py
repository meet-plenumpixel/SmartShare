from extra_views import InlineFormSetFactory
from account import models as account_model


class TransactionInlineFormSet(InlineFormSetFactory):
  model = account_model.Transaction
  fields = ('payer', 'borrower', 'group_through', 'amount')
  factory_kwargs = {
    'fk_name': 'payer',
    'extra': 1
  }

