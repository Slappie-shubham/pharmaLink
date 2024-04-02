from django.db import models
from accounts.models import User

# Create your models here.
class Stocks(models.Model):
    name = models.CharField(max_length=255)
    generic_name = models.CharField(max_length=255)
    dosage_strength = models.CharField(max_length=255)
    dose_form = models.CharField(max_length=255)
    manufacture_name = models.CharField(max_length=255)
    manufacture_date = models.DateField()
    stock = models.CharField(max_length=55)
    batch = models.CharField(max_length=55, default="0000")
    expiry_date = models.DateField()
    extra_detail = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = "Stocks"

    def __str__(self):
        return self.name    


class Report(models.Model):
    name = models.CharField(max_length=255)
    status = models.BooleanField(default=False)
    report = models.ImageField(upload_to="report")
    Date = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = "Report"

    def __str__(self):
        return self.name
    
class DoctorsPrescription(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="prescription", limit_choices_to={'is_customer': True})
    prescription = models.ImageField(upload_to="prescription")
    notes = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = "Doctor Prescription"

    def __str__(self):
        return self.user.first_name + self.user.last_name
    
class FAQ(models.Model):
    question = models.CharField(max_length=500)
    answer = models.TextField()

    class Meta:
        verbose_name = "FAQ"

    def __str__(self):
        return self.question



     
