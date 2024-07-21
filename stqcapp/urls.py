from django.contrib import admin
from django.urls import path
from stqcapp import views
# from .views import home


urlpatterns = [
    path('admin/', admin.site.urls),
    # path("",views.dash,name='dash'),
    # path ("about",views.about,name='about'),
    path("loginfinal",views.login,name='loginfinal'),
    path("dashboard",views.dashboard,name='dashboard'),
    path("dispatchform",views.dispatch,name='dispatchform'),
    path("edit_record/<int:id>/",views.edit_record,name='edit_record'),
    path('delete/<int:id>/', views.delete_record, name='delete_record'),
    path("receiveform",views.receive,name='receiveform'),
    path("getdispatchform",views.getdispatch,name='getdispatchform'),
 
    path('registration',views.registrationform,name='registration'),
    path('getregistration',views.getregist,name='getregistration'),
#look at the view.registrationform and the views.py def registrationform these names should be similar
    path('getreceive',views.getreceive,name='getreceive')

#i was fucking stuck with this problem for 3 4 days today i solved it on 24/6/24 by making the 
# class model and function name different and keeping the model names and def views left names similar ,
#also mentioning the views.registrationform here. thanks
]