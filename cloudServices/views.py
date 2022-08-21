from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.

from django.http import HttpResponse

from accounts.models import Project, Userdata




def home(request):
    return render(request,'home.html')



def about(request):
    return render(request,'about.html')

def faq(request):
    return render(request,'faq.html')

def help(request):
    return render(request,'help.html')

@login_required(login_url='/Signin')
def selectproject(request):
    # active=Project.objects.get(is_active=request.user.is_active)
    # active.is_active=False
    # print(active)
    # active.save()

    if request.method=='POST':
        project_name=request.POST['projectname']
        project_id=request.POST['projectid']
        if Project.objects.filter(project_id=project_id).exists():
            messages.warning(request,'Project ID Already Exists')
            return redirect("/selectproject")

        usr=User.objects.get(username=request.user.username)
        projectdata=Project(user=usr,project_id=project_id,project_name=project_name,is_active=True)
        projectdata.save()
        messages.success(request,'Your Projct Created Successfully')
        
        data=projectData(request)
        return render(request,'selectproject.html',data)
    else:
        data=projectData(request)
        return render(request,'selectproject.html',data)


def projectData(request):
    context = {}
    ch=Userdata.objects.filter(user__id=request.user.id)

    if len(ch)>0:
        data =Userdata.objects.get(user__id=request.user.id)
        context["data"] = data
    all = Project.objects.filter(user__id=request.user.id).order_by("-id")
    context["products"] = all

    #return redirect("/")
    return context    



    
