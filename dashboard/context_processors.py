from dashboard.models import *


def notification(request):
   notification = Notification.objects.filter(specific_user=request.user.id)[:5]
   count = Notification.objects.filter(specific_user=request.user.id).count()
   return {"notification": notification, "count":count}