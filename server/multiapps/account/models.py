from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
  image = models.ImageField(default='profile_pics/user_default.jpg', upload_to='profile_pics')
  total_balance = models.IntegerField(default=5000)
  total_credit = models.IntegerField(default=0)
  total_debit = models.IntegerField(default=0)

  class Meta:
    verbose_name = 'User'
    unique_together = (('username', 'email'),)
    ordering = ('username',)

  def __str__(self):
    return self.username


class UserGroup(models.Model):
  name = models.CharField(unique=True, max_length=30)
  owner = models.ForeignKey('account.User', related_name='my_groups', on_delete=models.PROTECT, limit_choices_to={'is_superuser': False})
  members = models.ManyToManyField(related_name='joined_groups', limit_choices_to={'is_superuser': False},
    to='account.User',
    through='account.LoanHistory',
    through_fields=('group_through','borrower')
  )

  class Meta:
    verbose_name = 'User Group'
    ordering = ('name',)

  def __str__(self):
    return self.name + 'group'


class LoanHistory(models.Model):
  borrower = models.ForeignKey(related_name='borrowed_transactions', on_delete=models.PROTECT, limit_choices_to={'is_superuser': False},
    to='account.User'
  )
  group_through = models.ForeignKey(related_name='group_transactions', on_delete=models.PROTECT,
    to='account.UserGroup'
  )
  have_to_pay = models.IntegerField(default=0)

  class Meta:
    verbose_name = 'Loan Transaction'

  def __str__(self):
    return f"borrower={self.borrower}, have_to_pay={self.have_to_pay}"

