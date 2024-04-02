from django.contrib import admin
from dashboard.models import (
    Stocks,
    Report,
    DoctorsPrescription,
    FAQ,
)

# Register your models here.
admin.site.register(Stocks)
admin.site.register(Report)
admin.site.register(DoctorsPrescription)
admin.site.register(FAQ)