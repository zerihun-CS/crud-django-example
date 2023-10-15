from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
   is_manager = models.BooleanField(default=False)

   is_customer = models.BooleanField(default=False)