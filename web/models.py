from django.db import models
from django.contrib.auth.models import User

class login_user(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.SET_NULL,null=True,blank =True)
    username2=models.CharField(max_length=25)
    password3=models.CharField( max_length=50)

    def __str__(self):
        return f"{self.username2}{self.password3}"
# Create your models here.

# from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

# class dispatchform(models.Model):
#     subject=models.CharField(max_length=100)
#     to=models.CharField(max_length=100)
#     address=models.CharField(max_length=100)
#     name = models.CharField(max_length=100)
#     date=models.DateField(null=True) #yyyy-mm-dd
#     track_id=models.CharField(max_length=100)
#     sent_by=models.CharField(max_length=100)
#     file_no=models.CharField(max_length=100)
#     remarks=models.CharField(max_length=100)

#     def __str__(self):
#         return f"{self.subject,self.to,self.address,self.name,self.date,self.track_id,self.sent_by,self.file_no,self.remarks}"

from django.db import models

class MyData(models.Model):
    # user = models.CharField( max_length=50)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    category = models.CharField(max_length=50)
    # user = models.CharField(max_length=100)


    def __str__(self):
        return f"{self.name,self.email,self.category}"


# models.py
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

