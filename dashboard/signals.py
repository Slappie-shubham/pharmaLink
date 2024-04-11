from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from dashboard.models import Stocks
from dashboard.models import orderemail
from django.conf import settings




@receiver(post_save, sender=Stocks)
def send_email(sender, instance, created, **kwargs):
   mail = orderemail.objects.all().first()
   if created or instance.stock < 10:
       if instance.stock < 10:
           subject = f"Low Stock Alert: {instance.name}"
           message = f'''The quantity of {instance.name} is less than 10 \n.
           Manufacture Date: {instance.manufacture_date},\n
           Expiry Date: {instance.expiry_date}\n
           Message from admin\n
           {mail.message}'''
           send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [mail.email,])
           



