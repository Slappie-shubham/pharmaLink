from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from accounts.models import User
from accounts.forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from accounts.forms import CustomPasswordChangeForm
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from django.http import Http404
from django.utils.http import urlsafe_base64_decode

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

def registration_success(request):
    return render(request, 'accounts/registration/registration_success.html')

def activation_success(request):
    return render(request, 'accounts/registration/activation_success.html')

def register_page(request):
    context = {}
    if request.user.is_authenticated:
        return redirect('dashboard:dashboard_page')
    
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.is_customer=True
            user.is_active = False
            user.username = form.cleaned_data.get('email')
            user.save()

            #creating activation link
            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            activation_link = f"http://localhost:8000/activate/{uidb64}/{token}"
            #composing mail
            subject_message = "Verify Account"
            message = render_to_string(
                "accounts/registration/activation_email.html",
                {
                    "activation_link" : activation_link,
                    "user" : user,
                },

            )
            #send mail
            email = EmailMessage(subject_message, message, settings.DEFAULT_FROM_EMAIL, [user.email])
            email.content_subtype = "html"
            email.send(fail_silently= False)
            messages.success(request, 'successfully registered')
            return redirect('accounts:register_success')
        print(form.errors, ".............")
    else:
        form = UserRegisterForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/register.html', context)

"user activation"
def activate_user(request, uidb64, token):
   try:
       uid = str(urlsafe_base64_decode(uidb64), 'utf-8')
       user = User.objects.get(id=uid)


       if user and default_token_generator.check_token(user, token):
           user.is_active = True
           user.save()
           return redirect('accounts:activation_success')
   except User.DoesNotExist:
       raise Http404("User not found or token is invalid.")
  
   except Exception as e:
       print(str(e))


   return render(request, 'accounts/registration/activation_failure.html')

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






        







    


