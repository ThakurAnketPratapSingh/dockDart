
from django.contrib import admin

from accounts.models import Project, Userdata, Userragistation
admin.site.site_header="dockDart"
admin.site.site_title="admin"
# Register your models here.

# class UserragistationAdmin(admin.ModelAdmin):
#    # fields=["username","first_name","email"]
  
#    list_display=["username","first_name","last_name","email","mobile","Designation","photo"]
#    search_fields=["username","mobile"]

class UserdataAdmin(admin.ModelAdmin):
   
#    # fields=["username","first_name","email"]
   list_display=["user","mobile","Designation","twitter","github","photo","update_on","added_on"]
   # search_fields=["mobile"]

class ProjectdataAdmin(admin.ModelAdmin):
   list_display=["user","project_name","project_id","date_on","is_active"]
   search_fields=["project_name","project_id"]




admin.site.register(Userdata,UserdataAdmin)
# admin.site.register(Userragistation,UserragistationAdmin)
admin.site.register(Project,ProjectdataAdmin)