from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
# Create your models here.


# class ProfileModel(models.Model):
#   user = models.OneToOneField(User, on_delete=models.CASCADE)

#   def __str__(self):
#     return f'{self.user.username} Profile'

class User(AbstractUser):
  image = models.ImageField(default='profile_pics/user_default.jpg', upload_to='profile_pics')
  phone_number = models.CharField(validators=[RegexValidator(regex=r"^(\+\d{1,3}[- ]?)?\d{10}$")], max_length=16, unique=True, blank=True)
  