from django.db import models

# Create your models here.


class Expense(models.Model):
  title = models.CharField(unique=True, max_length=50)
  detail = models.TextField(blank=True, max_length=200)
  amount = models.DecimalField(max_digits=6, decimal_places=2)
  pay_by = models.ForeignKey('account.UserAccount', related_name='paid_expenses', on_delete=models.PROTECT, limit_choices_to={'is_superuser': False})
  contributor = models.ManyToManyField('account.UserAccount', related_name='expense_contributor', limit_choices_to={'is_superuser': False})

  class Meta:
    verbose_name = 'Expense'
    ordering = ('pay_by', 'amount')

  def __str__(self):
    return self.title


class ExpenseGroup(models.Model):
  name = models.CharField(unique=True, max_length=30)
  owner = models.ForeignKey('account.UserAccount', related_name='my_groups', on_delete=models.PROTECT, limit_choices_to={'is_superuser': False})
  members = models.ManyToManyField('account.UserAccount', limit_choices_to={'is_superuser': False})

  class Meta:
    verbose_name = 'Expense Group'
    ordering = ('owner', 'name')

  def __str__(self):
    return self.name + 'group'
