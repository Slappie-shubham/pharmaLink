from django.db import models

# Create your models here.
class Medicine(models.Model):
    name = models.CharField(max_length=255)
    generic_name = models.CharField(max_length=255)
    dosage_strength = models.CharField(max_length=255)
    dose_form = models.CharField(max_length=255)
    manufacture_name = models.CharField(max_length=255)
    manufacture_date = models.DateField()
    expiry_date = models.DateField()
    extra_detail = models.TextField()


    class Meta:
        verbose_name = "Medicine"

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



     
