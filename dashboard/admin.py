from django.contrib import admin
from dashboard.models import *




# Register your models here.
admin.site.register(Stocks)
admin.site.register(Report)
admin.site.register(DoctorsPrescription)
admin.site.register(FAQ)
admin.site.register(Notification)
admin.site.register(Sales)


admin.site.register(Bills)
admin.site.register(BillsItems)
admin.site.register(orderemail)