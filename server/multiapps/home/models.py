from django.db import models
# Create your models here.

class Expense(models.Model):
  title = models.CharField(unique=True, max_length=50)
  detail = models.TextField(blank=True, max_length=200)
  amount = models.DecimalField(max_digits=6, decimal_places=2)
  date = models.DateTimeField(auto_now_add=True)
  group = models.ForeignKey(related_name='gp_expenses', on_delete=models.PROTECT,
    to='account.UserGroup'
  )

  class Meta:
    verbose_name = 'Expense'
    ordering = ('group', 'title')

  def __str__(self):
    return self.title

