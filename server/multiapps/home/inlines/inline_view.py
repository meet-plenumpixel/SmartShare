from extra_views import InlineFormSetFactory
from home import models as home_model

class ExpenseGroupInlineFormSet(InlineFormSetFactory):
  model = home_model.ExpenseGroup
  fields = ('name', 'owner')
  factory_kwargs = {
    # 'fk_name': 'payer',
    'extra': 1
  }
  
