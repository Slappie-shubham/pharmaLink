from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from accounts.forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from accounts.forms import CustomPasswordChangeForm


# Create your views here.
def login_page(request):
    if request.user.is_authenticated:
        return redirect ('dashboard:dashboard_page')

    if request.method=='POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request = request, email = email, password = password)#authenticating User
        if user is not None:
            login(request = request, user = user)
            return redirect ('dashboard:dashboard_page')
        else:
            messages.error(request, "Invalid Details")
            return redirect('accounts:login_page')
    return render(request,"accounts/login.html")

def register_page(request):
    context = {}
    if request.user.is_authenticated:
        return redirect('dashboard:dashboard_page')
    
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.is_customer=True
            user.username = form.cleaned_data.get('email')
            user.save()
            messages.success(request, "Sucessfully registered")
            #return redirect('accounts:login_page')
        print(form.errors, ".............")
    else:
        form = UserRegisterForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/register.html', context)

"""logout view"""
@login_required(login_url = '/')
def logout_process(request):
    logout(request)
    return redirect('accounts:login_page')

@login_required(login_url= '/')
def change_password(request):
    if request.method == "POST":
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Your password was successfully updated!')
            return redirect('dashboard:dashboard_page')
    else:
        form = CustomPasswordChangeForm(request.user)
    return render(request, "accounts/change_password.html", {"form" : form})






        







    


