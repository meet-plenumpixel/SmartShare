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

  def __str__(self):
    return self.username
