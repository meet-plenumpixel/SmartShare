from django.db.models import signals, F
from django.dispatch.dispatcher import receiver

from account.models import LoanHistory

# Create your signals here.

@receiver(signals.pre_save, sender=LoanHistory)
def repay_to_group_admin(sender, instance, **kwargs):
  if not kwargs['created']:
    existing_instance = sender.objects.get(pk=instance.id)

    existing_instance.borrower.total_balance -= instance.have_to_pay
    existing_instance.borrower.save(update_fields=['total_balance'])

    existing_instance.group_through.owner.total_balance += instance.have_to_pay
    existing_instance.group_through.owner.save(update_fields=['total_balance'])
    
    instance.have_to_pay = existing_instance.have_to_pay - instance.have_to_pay

