from django.contrib.auth import login, logout
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .form import Register_Form, Login_Form, Forget_Form, Reseat_Form
from .models import User
from django.utils.crypto import get_random_string
from utils.email_service import Email_Funk

# Create your views here.
class RegisterView(View):
    def get(self, request):
        form = Register_Form()
        return render(request , "account/register.html" , {"data":form})
    def post(self , request):
        form = Register_Form(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            passwd = form.cleaned_data.get('password')
            user : bool = User.objects.filter(email__exact=email).exists()
            if not user :
               new_user = User(email=email , username=username , is_active=False , email_active=get_random_string(94))
               new_user.set_password(passwd)
               Email_Funk("فعال ساز ایمیل" , new_user.email , {"user":new_user} , "active.html")
               new_user.save()
               return redirect(reverse("Index"))
            else :
                raise Http404("Your email is already exist!")
        else :
            raise Http404("Your Information is not valid")

class ActveCodeView(View):
    def get(self , request , code):
        user = User.objects.filter(email_active=code).first()
        if user is not None:
            if not user.is_active:
                user.is_active = True
                user.email_active = get_random_string(94)
                user.save()
                return redirect(reverse("Index"))
        else :
            raise Http404("We couldn't find the email")
class LoginView(View):
    def get(self , request):
        form = Login_Form()
        return render(request , "account/login.html" ,{"form":form})
    def post(self , request):
        form = Login_Form(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = User.objects.filter(email__exact=email).first()
            if user is not None:
                if user.is_active :
                    check = user.check_password(password)
                    if check:
                        login(request , user)
                        Email_Funk("به مجموعه سناتور خوس آدید" , user.email , {"user":user} , "welcome.html")
                        return redirect(reverse("Index"))
                    else :
                        raise Http404("Your password is not correct!")
                else :
                    raise Http404("Your account is not active")
            else :
                raise  Http404("We couldn't find your email")
class LogoutView(View):
    def get(self , request):
        logout(request)
        return redirect(reverse("Index"))
class ForgetView(View):
    def get(self , request):
        form = Forget_Form()
        return render(request, "account/forget.html" , {"form":form})
    def post(self , request):
        form = Forget_Form(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            user = User.objects.filter(email__exact=email).first()
            if user is not None:
                user.email_active = get_random_string(94)
                Email_Funk("تغییر رمز" , user.email , {"user":user} , "Change_passwd.html")
                user.save()
                return redirect(reverse("Index"))
class ReseatView(View):
    def get(self , request , code):
        user = User.objects.filter(email_active__iexact=code).first()
        if user is not None:
            form = Reseat_Form()
            return render(request , "account/reseat_passwd.html" , {"form": form})
        else :
            raise Http404("We couldn't find your emial")
    def post(self , request , code):
        form = Reseat_Form(request.POST)
        if form.is_valid():
            user = User.objects.filter(email_active__iexact=code).first()
            if user is not None:
                passwd = form.cleaned_data.get("password")
            user.set_password(passwd)
            user.save()
            return redirect(reverse("Index"))