from django.db.models import signals, F
from django.dispatch.dispatcher import receiver

from home.models import Expense

# Create your signals here.

@receiver(signals.post_save, sender=Expense)
def split_expence_with_group_members(sender, instance, **kwargs):
  group_owner = instance.group.owner
  group_owner.total_balance -= instance.amount
  group_owner.save(update_fields=['total_balance'])

  loan_transactions = instance.group.group_transactions
  expence_per_member = instance.amount / (loan_transactions.count()+1)
  loan_transactions.all().update(have_to_pay=F('have_to_pay')+expence_per_member)