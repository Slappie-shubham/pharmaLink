from django.db import models
from django.contrib.auth.models import AbstractUser           
# Create your models here.


class User(AbstractUser):
   email = models.EmailField(unique=True, verbose_name = 'email')
   is_employee = models.BooleanField(default=False)
   is_customer = models.BooleanField(default=False)
   phone = models.CharField(max_length=255, null=True, blank=True)
   address = models.CharField(max_length=255, null=True, blank=True)
   dob = models.DateField(null=True, blank=True)
   profile_pic = models.ImageField(upload_to='profile', default='profile/user.jpg')
  


  
   USERNAME_FIELD = "email"
   REQUIRED_FIELDS = "username","first_name","last_name"