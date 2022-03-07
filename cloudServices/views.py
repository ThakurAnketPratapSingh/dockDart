from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def home(request):
    return render(request,'home.html')

def signUp(request):
    return render(request,'login.html')

def about(request):
    return render(request,'about.html')

def faq(request):
    return render(request,'faq.html')

def help(request):
    return render(request,'help.html')

    
