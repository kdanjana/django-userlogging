from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View

from .forms import UserSignUpForm, LoginForm
from .models import User
# Create your views here.


def main_page(request):
    return render(request, "mainapp/main.html")

class SignupPage(View):
    def get(self, request):
        return render(request, "mainapp/signup.html", {"form": UserSignUpForm()})
    
    def post(self,request):
        submitted_form = UserSignUpForm(request.POST or None)
        err_mssg = ""
        if submitted_form.is_valid():
            username = submitted_form.cleaned_data.get('user_name')
            user_email = submitted_form.cleaned_data.get('email')
            if len(User.objects.filter(user_name=username)) != 0 or len(User.objects.filter(email=user_email)) != 0:
                err_mssg = 'User already exists.'
                return render(request, "mainapp/signup.html", {
                    "form": UserSignUpForm(),
                    "error_mssg": err_mssg
                })
            else:
                submitted_form.save()
                return HttpResponseRedirect("/sp_success/")
        else:
            return render(request, "mainapp/signup.html", {
                "form": submitted_form,
                "error_mssg": err_mssg
                })

def signup_success(request):
    return render(request, "mainapp/signup_success.html")


class LoginPage(View):
    def get(self, request):
        return render(request, "mainapp/login.html", {"form": LoginForm()})

    def post(self, request):
        submitted_form = LoginForm(request.POST or None)
        error_mssg = ""
        if submitted_form.is_valid():
            username = submitted_form.cleaned_data.get('user_name')
            pass_word = submitted_form.cleaned_data.get('password')
            
            if len(User.objects.filter(user_name=username)) == 0 :
                error_mssg = "Wrong user name or password."
            elif pass_word != User.objects.get(user_name=username).password:
                error_mssg = "Wrong password or password."
        if error_mssg == "":
            return HttpResponseRedirect("/ln_success/")
        else:
            return render(request, "mainapp/login.html", {
                "form": LoginForm(),
                "error": error_mssg
            })
        

def login_success(request):
    return render(request, "mainapp/login_success.html")


def LogoutPage(request):
    return render(request, "mainapp/logout.html")
