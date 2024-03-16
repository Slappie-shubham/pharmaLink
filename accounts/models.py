from django.db import models
from django.contrib.auth.models import AbstractUser            
# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name = 'email')
    is_employee = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)

    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = "first_name","last_name"