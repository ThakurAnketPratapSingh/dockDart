from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse




def home(request):
    return render(request,'home.html')



def about(request):
    return render(request,'about.html')

def faq(request):
    return render(request,'faq.html')

def help(request):
    return render(request,'help.html')

def docimg(request):
    return render(request,'docimg.html')

def selectproject(request):
    return render(request,'selectproject.html')

def webdock(request):
    return render(request,'webdock.html')

    
