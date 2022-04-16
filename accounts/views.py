from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User , auth

from django.views.generic import TemplateView
class Home(TemplateView):
    template_name = "home.html"

def signUp(request):
    if request.method=='POST':
        first_name=request.POST['fname']
        last_name=request.POST['lname']
        username=request.POST['username']
        password1=request.POST['pass1']
        password2=request.POST['pass2']
        email=request.POST['email']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,'Username Already Exists')
                return redirect('/Signup')
            elif User.objects.filter(email=email).exists():
                messages.error(request,'Email Already Exists')
                return redirect('/Signup')

            elif len(username)>10:
                messages.error(request,'Username must be under 10 characters')
                return redirect('/Signup')
            elif not username.isalnum():
                messages.error(request,'Username should only contains letters and numbers')
                return redirect('/Signup')
            elif len(password1)<8:
                messages.error(request,'Password should be of atlest 8 characters')
                return redirect('/Signup')
            else:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                messages.success(request,'User Successfully Created')
        else:
            messages.error(request,'Password Not Matching')
            return redirect('/Signup')
        return redirect('/')
    else:
        return render(request,'signup.html')


def signIn(request):
    if request.method=='POST':
        loginusername=request.POST['username']
        loginpassword=request.POST['pass']
        user=authenticate(username=loginusername,password=loginpassword)

        if user is not None:
            login(request,user)
            messages.success(request,"Successfully Logged In")
            return redirect('/')

        else:
            messages.error(request,"Invalid Email/Password, Please Try Again.")
            return redirect('/Signin')
    return render(request,'signin.html')

def Logout(request):
    logout(request)
    messages.success(request,"Successfully Logged Out")
    return redirect('/')