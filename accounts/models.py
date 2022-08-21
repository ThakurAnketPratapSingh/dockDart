from email.policy import default
import datetime
from multiprocessing.sharedctypes import Value
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Userragistation(models.Model):
    
    username=models.CharField(max_length=100, primary_key=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=200, unique=True)
    mobile=models.IntegerField(default="9161153581")
    Designation=models.TextField(default="student")
    password = models.CharField(max_length=50)
    photo=models.ImageField(default='')
    twitter=models.CharField(max_length=250, default="@twiter")
    github=models.CharField(max_length=250, default="@github")
    added_on=models.DateTimeField(auto_now_add=True,null=True)
    update_on=models.DateTimeField(auto_now=True,null=True)
    def __str__(self) :
        return self.first_name+" "+self.last_name+", "+"user_name =  "+self.username

class Userdata(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)   
    mobile=models.IntegerField(default="9161153581")
    Designation=models.TextField(default="student")  
    photo=models.ImageField(upload_to = "profiles/%Y/%m/%d",null=True,blank=True)
    twitter=models.CharField(max_length=250, default="@twiter")
    github=models.CharField(max_length=250, default="@github")
    added_on=models.DateTimeField(default=datetime.datetime.now())
    update_on=models.DateTimeField(default=datetime.datetime.now())
    def __str__(self) :
        return self.user.username


class Project(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    project_id=models.CharField(max_length=250,blank=True,null=True)
    project_name=models.CharField(max_length=250,blank=True,null=True)
    is_active=models.BooleanField(default=False)
    date_on=models.DateTimeField(default=datetime.datetime.now())
    def __str__(self) :
        return self.user.username

