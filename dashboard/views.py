from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from dashboard.models import Medicine

# Create your views here.
@login_required(login_url='/')
def dashboard_page(request):
    medicine = Medicine.objects.all()
    context = {
        'medicine' : medicine
    }
    return render(request,'dashboard/dashboard.html', context)