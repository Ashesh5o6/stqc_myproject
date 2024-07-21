from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class registration(models.Model):
    Names=models.CharField(max_length=30)
    Designations=models.CharField(max_length=30)
    Usernames=models.CharField(max_length=30)
    Passwords=models.CharField(max_length=30)
    #used to make the table in admin server 
    def __str__(self):
        return f"{self.Names}{self.Designations}{self.Usernames}{self.Passwords}"
    
class category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class dispatchform(models.Model):
    subject=models.CharField(max_length=100)
    to=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    dispatch_by=models.CharField(max_length=100)
    date=models.DateField(null=True) #yyyy-mm-dd
    track_id=models.CharField(max_length=100)
    sent_by=models.CharField(max_length=100)
    file_no=models.CharField(max_length=100)
    remarks=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.subject,self.to,self.address,self.dispatch_by,self.date,self.track_id,self.sent_by,self.file_no,self.remarks}"

class receiveform(models.Model):
    Subject=models.CharField(max_length=100)
    From=models.CharField(max_length=100)
    To=models.CharField(max_length=100)
    Receive_date=models.DateField(null=True) 
    Received_by=models.CharField(max_length=100)
    File_no=models.CharField(max_length=100)
    Remarks=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.Subject,self.From,self.To,self.Receive_date,self.Received_by,self.File_no,self.Remarks}"
    

# class login_user(models.Model):
#     user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True,blank =True)
#     username=models.CharField(max_length=25)
#     password=models.CharField( max_length=50)

#     def _str_(self):
#         return f"{self.username}{self.password}"
