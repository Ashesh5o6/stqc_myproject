from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login ,logout
from stqcapp.models import registration,dispatchform,receiveform,category
#this was imported from the models
# from .models import registratio
from django.contrib.auth.models import User 

from .form import eddispatches
from django.contrib import messages

# Create your views here.
# def dash(request):
    
#     return HttpResponse("dash page")

def dashboard(request):
    entry_count = dispatchform.objects.count()
    entry_count2 =receiveform.objects.count()
    user_count= registration.objects.count()
    context = {'entry_count': entry_count,
               'entry_count2': entry_count2,
               'user_count': user_count}
    # context2= {'entry_count2': entry_count2}
    return render(request,'dashboardfinal.html',context)

from django.shortcuts import render
from .models import dispatchform  # Replace with your actual model name

# def home(request):
#     entry_count = dispatchform.objects.count()
#     context = {'entry_count': entry_count}
#     return render(request, 'dashboard.html', context)

def login(request): 
    if request.method=="POST":
        username= request.POST.get('username')
        password= request.POST.get('password')
        print(username)
        print(password)

        myuser=authenticate(username=username,password=password)

        if myuser is None:
            messages.error(request,'Invalid credential')
            return redirect('login')
            
        else:
            login(request,myuser)
            return render(request,'dashboardfinal.html')
    
    
    return render(request,'loginfinal.html')
def registrationform(request):
    if request.method=="POST":
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        username = request.POST.get("username")
        password = request.POST.get("password")

        user=User.objects.filter(username=username)

        if user.exists():
            messages.info(request,'user name already taken')
            return redirect('registration')
    
        user = User.objects.create_user(first_name=first_name, last_name=last_name ,username=username )
        # User.objects.create_user will be used  
        user.set_password(password)
        user.save()
        messages.info(request,'Account created successfully')



        return redirect('registration')
        # reg=registration(Names=Name,Designations=Designation,Usernames=Username,Passwords=Password)
        # reg.save()
        #left names are the model names and right are the def functions variable in this .
        #in brackets are the names of the name=" " of the form in html file
        #**name of the class of the models should be different from def name of view

    return render(request,'registration.html')

def dispatch(request):
    categories = category.objects.all()

    if request.method=="POST":
        subject=request.POST.get('subject')
        to=request.POST.get('to')
        address=request.POST.get('address')
        dispatch_by=request.POST.get('dispatch_by')
        date=request.POST.get('date')
        track_id=request.POST.get('track_id')
        sent_by=request.POST.get('sent_by')
        file_no=request.POST.get('file_no')
        remarks=request.POST.get('remarks')

        disp=dispatchform(subject=subject,to=to,address=address,dispatch_by=dispatch_by,date=date,track_id=track_id,sent_by=sent_by,file_no=file_no,remarks=remarks)
        disp.save()
    
    return render(request,'dispatchfinal.html', {'categories': categories})

from django.shortcuts import render, get_object_or_404, redirect
from .models import dispatchform

def category_view(request):
    categories = category.objects.all()
    return render(request, 'dispatchform.html', {'categories': categories})

def edit_record(request, id):
    # categories = category.objects.all()
    edit = dispatchform.objects.get(id=id)
    form= eddispatches(request.POST,instance=edit)
    if form.is_valid():
        form.save()
    
    return render(request, 'edit_dispatch.html', {'edit': edit})

def delete_record(request, id):
        dispatch = get_object_or_404(dispatchform, id=id)
        if request.method == 'POST':
            dispatch.delete()
            return redirect('getdispatchform')  
        messages.success(request,"Deleted successfully")
        return render(request, 'confirm_delete.html', {'dispatch': dispatch})

# def update_record(request, id):
#     update = dispatchform.objects.get(id=id)
#     form= eddispatches(request.POST,instance=update)
#     if form.is_valid():
#         form.save()
    
#     return render(request, 'edit_dispatch.html', {'update': update})



def getregist(request):
    get_data_reg=registration.objects.all()
    # for a in get_data_reg:
    #     print(a.Names)
    # print(registration)
    data1={
        'registration':get_data_reg
    }
    return render(request,'getregistration.html',data1)

def getdispatch(request):
    get_data_dis=dispatchform.objects.all()
    # for b in get_data_dis:
    #     print(b.subject)
    # print(dispatchform)
    data3={
        'dispatchForm':get_data_dis
    }
    return render(request,'data.html',data3)

def getreceive(request):
    get_data_rec=receiveform.objects.all()
    # for b in get_data_dis:
    #     print(b.subject)
    # print(dispatchform)
    data3={
        'receiveForm':get_data_rec
    }
    return render(request,'getreceive.html',data3)


def receive(request):
    if request.method=="POST":

        Subject=request.POST.get('subject')
        From=request.POST.get('from')
        To=request.POST.get('to')
        Receive_date=request.POST.get('Receive date')
        Received_by=request.POST.get('Received by')
        File_no=request.POST.get('file_no')
        Remarks=request.POST.get('Remarks')

        resp=receiveform(Subject=Subject,From=From,To=To,Receive_date=Receive_date,Received_by=Received_by,File_no=File_no,Remarks=Remarks)
        resp.save()
        messages.success(request,"Deleted successfully")
        
    return render(request,'receivefinal.html')

