from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User , auth
# Create your views here.
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
                return redirect('/login')
            elif User.objects.filter(email=email).exists():
                messages.error(request,'Email Already Exists')
                return redirect('/login')

            elif len(username)>10:
                messages.error(request,'Username must be under 10 characters')
                return redirect('/login')
            elif not username.isalnum():
                messages.error(request,'Username should only contains letters and numbers')
                return redirect('/login')
            elif len(password1)<8:
                messages.error(request,'Password should be of atlest 8 characters')
                return redirect('/login')
            else:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save();
                messages.success(request,'User Successfully Created')
        else:
            messages.error(request,'Password Not Matching')
            return redirect('/login')
        return redirect('/')
    else:
        return render(request,'signup.html')


def signIn(request):
    return render(request,'signin.html')