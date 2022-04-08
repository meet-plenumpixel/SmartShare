from django.db import models
# Create your models here.

class Expense(models.Model):
  title = models.CharField(unique=True, max_length=50)
  detail = models.TextField(blank=True, max_length=200)
  amount = models.DecimalField(max_digits=6, decimal_places=2)
  group = models.ForeignKey(related_name='gp_expenses', on_delete=models.PROTECT,
    to='ExpenseGroup'
  )

  class Meta:
    verbose_name = 'Expense'
    ordering = ('group', 'title')

  def __str__(self):
    return self.title


class ExpenseGroup(models.Model):
  name = models.CharField(unique=True, max_length=30)
  owner = models.ForeignKey('account.User', related_name='my_groups', on_delete=models.PROTECT, limit_choices_to={'is_superuser': False})
  members = models.ManyToManyField(related_name='joined_groups', limit_choices_to={'is_superuser': False},
    to='account.User',
    through='account.Transaction',
    through_fields=('group_through','borrower')
  )

  class Meta:
    verbose_name = 'Expense Group'
    ordering = ('name',)

  def __str__(self):
    return self.name + 'group'
