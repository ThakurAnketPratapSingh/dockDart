from django.shortcuts import render,redirect
from django.contrib import messages
# Create your views here.
from subprocess import getoutput as go
from django.http import HttpResponse

def webdock(request):
    if request.method=='POST':
        command=request.POST['cmd']
        btn=request.POST['contimg']
        if btn=='run':
            if "docker" in command :
                status = go(f"sudo {command}")
                messages.success(request,status)
                return redirect('/dockrun')
            else :
                messages.success(request,'ONLY DOCKER COMMANDS ALLOWED, TRY AGAIN')
                return redirect('/dockrun')

        elif btn=='showimg':
            status = go("sudo docker images")
            messages.success(request,status)
            return redirect('/dockrun')

        elif btn=='container':
            status = go("sudo docker ps")
            messages.success(request,status)
            return redirect('/dockrun')
   
    return render(request,'webdock.html')

def docimg(request):
    if request.method=='POST':
        code=request.POST['dockcode']
        imagename=request.POST['imgname']
        imageversion=request.POST['imgversion']
        username=request.POST['user']
        password=request.POST['pass']
        status = go('sudo mkdir /dockerfiles')
        path = f'/dockerfiles/{imagename}'
        status = go(f'sudo mkdir {path}')
        status = go(f'sudo touch {path}/Dockerfile')
        status = go(f'sudo chown apache {path}/Dockerfile')
        status = go(f'sudo echo "{code}" > {path}/Dockerfile')
        status = go(f'sudo dos2unix {path}/Dockerfile')
        status = go('sudo systemctl start docker')
        status = go(f'sudo docker build -t {username}/{imagename}:{imageversion} {path}')
        status = go(f'sudo docker login -u {username} -p {password}') 
        status = go(f'sudo docker push {username}/{imagename}:{imageversion}')
        messages.success(request,status)
        return redirect('/dockfile')
    return render(request,'docimg.html')
