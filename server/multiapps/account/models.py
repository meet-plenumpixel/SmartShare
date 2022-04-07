from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib import admin
# Create your models here.


class User(AbstractUser):
  image = models.ImageField(default='profile_pics/user_default.jpg', upload_to='profile_pics')
  total_balance = models.IntegerField(default=0)
  total_credit = models.IntegerField(default=0)
  total_debit = models.IntegerField(default=0)

  class Meta:
    verbose_name = 'User'
    unique_together = (('username', 'email'),)
    ordering = ('username',)

  def __str__(self):
    return self.username



class Transaction(models.Model):
  payer = models.ForeignKey(related_name='paid', on_delete=models.PROTECT, limit_choices_to={'is_superuser': False},
    to='account.User'
  )
  borrower =models.ForeignKey(related_name='borrowed', on_delete=models.PROTECT, limit_choices_to={'is_superuser': False},
    to='account.User'
  )
  group_through = models.ForeignKey(on_delete=models.PROTECT,
    to='home.ExpenseGroup'
  )

  amount = models.IntegerField(default=0)
  return_status = models.BooleanField(default=False, choices=((True, 'complete'), (False, 'pending')))

  class Meta:
    verbose_name = 'Transaction'

  def __str__(self):
    return f"payer={self.payer}, borrower={self.borrower}, amount={self.amount}"




