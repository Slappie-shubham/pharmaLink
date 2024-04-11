from django.db import models
from accounts.models import User


class Stocks(models.Model):
    name = models.CharField(max_length=255)
    generic_name = models.CharField(max_length=255)
    dosage_strength = models.CharField(max_length=255)
    dose_form = models.CharField(max_length=255)
    manufacture_name = models.CharField(max_length=255)
    manufacture_date = models.DateField()
    stock = models.IntegerField()
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
    customer_notes = models.TextField(null=True, blank=True)
    employee_notes = models.TextField(null=True, blank=True)
    status = models.BooleanField(default=False)
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
 


class Notification(models.Model):
    notification = models.CharField(max_length=1000)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    specific_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='specific_notifcation')
    created_date = models.DateTimeField(auto_now_add=True)




    def __str__(self):
      return self.notification
    class Meta:
      verbose_name = "notifications"


class Sales(models.Model):
    name = models.CharField(max_length=255)
    generic_name = models.CharField(max_length=255)
    dosage_strength = models.CharField(max_length=255)
    dose_form = models.CharField(max_length=255)
    manufacture_name = models.CharField(max_length=255)
    manufacture_date = models.DateField()
    qty = models.CharField(max_length=55)
    price = models.IntegerField()
    batch = models.CharField(max_length=55, default="0000")
    expiry_date = models.DateField()
    extra_detail = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = "sales"


    def __str__(self):
        return self.name
 
class Bills(models.Model):
   customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='billspatient', limit_choices_to={'is_customer': True} )
   prescription = models.OneToOneField(DoctorsPrescription, on_delete=models.CASCADE, related_name='DoctorsPrescription')
   bill_no = models.IntegerField(unique=True)
   created_date = models.DateTimeField(auto_now_add=True)
   sub_total = models.CharField(max_length=10)
   discount = models.CharField(max_length=10)
   net_amount = models.CharField(max_length=10)
   paid_status = models.BooleanField(default=False)
   generated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='generated', limit_choices_to={'is_employee': True})
   class Meta:
       verbose_name = 'bill'


   def __str__(self):
       return self.customer.first_name + self.customer.last_name + ":billno" + str(self.bill_no)
  
class BillsItems(models.Model):
   bills = models.ForeignKey(Bills, on_delete=models.CASCADE, related_name='billitem')
   description = models.CharField(max_length=255)
   qty = models.CharField(max_length=255, null=True, blank=True)
   amount = models.IntegerField()


   class Meta:
       verbose_name = 'billitem'


   def __str__(self):
       return self.bills.customer.first_name + self.bills.customer.last_name
  


class orderemail(models.Model):
   name = models.CharField(max_length=255)
   email = models.EmailField()
   message = models.TextField()
   class Meta:
       verbose_name = 'orderemail'


   def __str__(self):
       return self.name
  

