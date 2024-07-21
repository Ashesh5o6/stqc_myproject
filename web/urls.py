from django.contrib import admin
from django.urls import path,include
from web import views
# from .views import home
from django.urls import path
from . import views

urlpatterns = [
   path('user_login5/', views.login_user, name='login5'),
   path('user_registration/',views.register_user, name='registe5'),
   path('dropdown/',views.category_view,name='dropdown'),
   path('dash/',views.dash,name='dash'),
   
#    path('dropdown',views.dropdown,name='dropdown'),



#i was fucking stuck with this problem for 3 4 days today i solved it on 24/6/24 by making the 
# class model and function name different and keeping the model names and def views left names similar ,
#also mentioning the views.registrationform here. thanks

# urls.py



    # path('', views.item_list, name='item_list'),
    # path('edit/<int:id>/', views.edit_item, name='edit_item')
]



