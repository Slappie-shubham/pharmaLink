from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def login_page(request):
    if request.user.is_authenticated:
        pass

    if request.method=='POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request = request, email = email, password = password)
        if user is not None:
            login(request = request, user = user)
            return redirect ('dashboard:dashboard_page')
        else:
            return redirect('accounts:login_page')
    return render(request,"accounts/login.html")
