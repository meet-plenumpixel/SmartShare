from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserAccount(AbstractUser):
  balance = models.DecimalField(default=0, max_digits=15, decimal_places=2)
  image = models.ImageField(default='profile_pics/user_default.jpg', upload_to='profile_pics')

  class Meta:
    verbose_name = 'User Account'
    unique_together = (('username', 'email'),)
    ordering = ('username',)


class UserExpense(models.Model):
  title = models.CharField(unique=True, max_length=50)
  detail = models.TextField(blank=True, max_length=200)
  amount = models.DecimalField(max_digits=6, decimal_places=2)
  pay_by = models.ForeignKey('UserAccount', related_name='paid_expenses', on_delete=models.PROTECT)
  contributor = models.ManyToManyField('UserAccount', related_name='expense_contributor')

  class Meta:
    verbose_name = 'User Expense'
    ordering = ('pay_by', 'amount')



class UserGroup(models.Model):
  name = models.CharField(unique=True, max_length=30)
  owner = models.ForeignKey('UserAccount', related_name='my_groups', on_delete=models.PROTECT)
  members = models.ManyToManyField('UserAccount')

  class Meta:
    verbose_name = 'User Group'
    ordering = ('owner', 'name')