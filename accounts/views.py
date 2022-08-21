from datetime import datetime
from multiprocessing import context
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from django.contrib.auth.forms import AuthenticationForm
from accounts.models import Project, Userragistation, Userdata

from django.views.generic import TemplateView
class Home(TemplateView):
    template_name = "home.html"

@login_required(login_url='/Signin')
def profilEditData(request):
    context={}
    data=Userdata.objects.get(user__id=request.user.id)
    context["data"]=data
    if request.method=="POST":
        first_name=request.POST['fname']
        last_name=request.POST['lname']
        email=request.POST['email']
        mobile=request.POST['phone']
        github=request.POST['git']
        twitter=request.POST['twit']
        desig=request.POST['desi']

        
        usr=User.objects.get(id=request.user.id)
        usr.first_name=first_name
        usr.last_name=last_name
        usr.email=email
        usr.save()

        data.mobile=mobile
        data.Designation=desig
        data.twitter=twitter
        data.github=github
        data.update_on=datetime.now()
        data.save()
        if "image" in request.FILES:
            img=request.FILES["image"]
            data.photo=img
            data.save()
        messages.success(request,'Profile Updated Successfully')
       
        return redirect('/profileWithData')
 
   # return render(request,'profilEditData.html')
    else :
        return render(request,'profilEditData.html')

@login_required(login_url='/Signin')
def profileWithData(request):
    return render(request,'profileWithData.html')

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
                messages.warning(request,'Username Already Exists')
                return redirect('/Signup')
            elif User.objects.filter(email=email).exists():
                messages.warning(request,'Email Already Exists')
                return redirect('/Signup')

            elif len(username)>10:
                messages.warning(request,'Username must be under 10 characters')
                return redirect('/Signup')
            elif not username.isalnum():
                messages.warning(request,'Username should only contains letters and numbers')
                return redirect('/Signup')
            elif len(password1)<8:
                messages.warning(request,'Password should be of atlest 8 characters')
                return redirect('/Signup')
            else:
                data=Userragistation(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                myuser=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                myuser.save()
                userdata=Userdata(user=myuser)
               # projectdata=Project(user=myuser)

                userdata.save()
                data.save()
                
        else:
            messages.warning(request,'Password Not Matching')
            return redirect('/Signup')
        return redirect('/selectproject')
    else:
        return render(request,'signup.html')


def signIn(request):
    if request.method=='POST':
        loginusername=request.POST['username']
        loginpassword=request.POST['pass']
        user=authenticate(username=loginusername,password=loginpassword)

        if user is not None:
            login(request,user)
            if user.is_superuser:
                return redirect("/admin")
            else :
                messages.success(request,"Successfully Logged In")
                return redirect('/selectproject')

        else:
            messages.warning(request,"Invalid User Name/Password, Please Try Again.")
            return redirect('/Signin')
    return render(request,'signin.html')
@login_required(login_url='/Signin')
def Logout(request):
    logout(request)
    messages.success(request,"Successfully Logged Out")
    return redirect('/')