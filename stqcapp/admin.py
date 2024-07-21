from django.contrib.admin.sites import site
from django.contrib import admin
from .models import registration,dispatchform,receiveform,category
#imported from app model

class modelhead1(admin.ModelAdmin):
    list_display=('Names','Designations','Usernames','Passwords')

    # def Names(self,obj):
    #     return obj.Names
    # Names.short
    
    # def Designations(self,obj):
    #     return obj.Designations
    
    # def Usernames(self,obj):
    #     return obj.Usernames
    
    # def Passwords(self,obj):
    #     return obj.Passwords

    # used to make the main heading row of the table


class modelhead2(admin.ModelAdmin):
    list_display=('subject','to','address','dispatch_by','date','track_id','sent_by','file_no','remarks')

admin.site.register(registration,modelhead1)

admin.site.register(dispatchform,modelhead2)

class modelhead3(admin.ModelAdmin):
    list_display=('Subject','From','To','Receive_date','Received_by','File_no','Remarks')

admin.site.register(receiveform,modelhead3)

admin.site.register(category)

#** remember this that after you make the models and register in the views page you also need to register in to the admin.py tooo***
#registration-name of the class in model