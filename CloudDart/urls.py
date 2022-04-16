"""CloudDart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


from cloudServices import views  as cs
from accounts import views as ac

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',cs.home),
    path("accounts/", include("allauth.urls")),
    path('Signup',ac.signUp),
    path('Signin',ac.signIn),
    path('Logout',ac.Logout),
    path('about',cs.about),
    path('faq',cs.faq),
    path('help',cs.help),
    path('dockfile',cs.docimg),
    path('selectproject',cs.selectproject),
    path('dockrun',cs.webdock),
    path("", ac.Home.as_view(), name="home"),


]
