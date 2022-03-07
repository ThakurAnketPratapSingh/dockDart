from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def home(request):
    return render(request,'home.html')

def signup(request):
    return render(request,'login.html')
    
