from django.contrib import admin
from dashboard.models import (
    Medicine,
    Report,
)

# Register your models here.
admin.site.register(Medicine)
admin.site.register(Report)