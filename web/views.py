from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login ,logout
from django.contrib import messages
# Create your views here.
from django.contrib.auth.models import User 
# from django.contrib.auth import authenticate,lo



def login_user(request): 
    if request.method=="POST":
        username= request.POST.get('username')
        password= request.POST.get('password')
        print(username)
        print(password)


        # if User.objects.filter(username=username).exists():
        #     messages.error(request,'Invalid Username')
        #     return redirect('login')

        myuser=authenticate(username=username,password=password)

        if myuser is None:
            messages.error(request,'Invalid credential')
            return redirect('login')
            
        else:
            login(request,myuser)
            return render(request,'dropdown.html')
    
    
    return render(request,'web/authenticate/loginb.html')

def register_user(request):

    if request.method =="POST":
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        username = request.POST.get("username")
        password = request.POST.get("password")

        print(first_name)
        print(last_name)
        print(username)
        print(password)

        user=User.objects.filter(username=username)

        if user.exists():
            messages.info(request,'user name already taken')
            return redirect('register')
    
        user = User.objects.create_user(first_name=first_name, last_name=last_name ,username=username )
        # User.objects.create_user will be used  
        user.set_password(password)
        user.save()
        messages.info(request,'Account created successfully')



        return redirect('register')
    #in redirect you can use the name(name is recommonded) and the urls path / to use this function

    return render(request,'web/authenticate/webregister.html')

from django.shortcuts import render, redirect



# views.py
from django.shortcuts import render
from .models import Category

# from web.models import dispatchform

# Category.objects.create(name='Category 1')
# Category.objects.create(name='Category 2')
# Add more categories as needed


def category_view(request):
    categories = Category.objects.all()
    return render(request, 'dropdown2.html', {'categories': categories})

# def dispatch(request):
#     if request.method=="POST":

#         subject=request.POST.get('subject')
#         to=request.POST.get('to')
#         address=request.POST.get('address')
#         name=request.POST.get('dispatch_by')
#         date=request.POST.get('date')
#         track_id=request.POST.get('track_id')
#         sent_by=request.POST.get('sent_by')
#         file_no=request.POST.get('file_no')
#         remarks=request.POST.get('remarks')

#         disp=dispatchform(subject=subject,to=to,address=address,name=name,date=date,track_id=track_id,sent_by=sent_by,file_no=file_no,remarks=remarks)
#         disp.save()
    
#     categories = dispatchform.objects.all()
#     return render(request, 'dropdown2.html', {'categories': categories})

from django.shortcuts import render, redirect
from .models import MyData

def submit_data(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        category = request.POST['category']
        # user = request.POST['user'] 
        # Data validation (optional)
        print(name)
        # print(user)

        new_data = MyData.objects.create(name=name, email=email, category=category)
        new_data.save()
        
        return redirect('success_page')  # Replace 'success_page' with your success page URL pattern name
    else:
        return render(request, 'dropdown2.html')


from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Item
from .forms import ItemForm
 
def item_list(request):
    items = Item.objects.all()
    return render(request, 'edit.html', {'items': items})

def edit_item(request, id):
    item = get_object_or_404(Item, id=id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
    else:
        form = ItemForm(instance=item)
    return render(request, 'confirm.html', {'form': form, 'id': id})

def dash(request):
    return render(request,'web/dash.html')