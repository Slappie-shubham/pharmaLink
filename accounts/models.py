from django.db import models
from django.contrib.auth.models import AbstractUser            
# Create your models here.

class User(AbstractUser):
    is_employee = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = "email","first_name","last_name"