from django.contrib import admin
from django.contrib import admin
from web.models import login_user
from web.models import Category
from web.models import MyData
from web.models import Item



# Register your models here.
admin.site.register(login_user)
admin.site.register(Category)
admin.site.register(MyData)
admin.site.register(Item)

