from django.shortcuts import render,redirect
from .models import Users
# Create your views here.
def index(request): 
    
    data ={
        "users": Users.objects.all(),
    }
    return render(request,'index.html',data)


def add_user(request): 
    if request.method == "POST" : 
        print(request.POST)
        if request.POST['first_name'] != '' : 
            fname = request.POST['first_name']
        if  request.POST['last_name'] != '' :    
            lname = request.POST['last_name']
        if  request.POST['email'] != '' :       
            email = request.POST['email']
        if  request.POST['age'] != '' and request.POST['age'].isnumeric(): 
                 age = int(request.POST['age'])
        
        newuser = Users.objects.create(first_name=fname , last_name=lname,email_address=email,age=age)         
        
    return  redirect('/')    

def delete(request,id): 
    del_user = Users.objects.get(id=id) 
    del_user.delete()
    return  redirect('/')   

def edit(request,id): 
    edit_user = Users.objects.get(id=id)
    data = {
        "user":edit_user, 
    }
    return  render(request,'editUser.html',data)  

def editUser (request,id) : 
    if request.method == "POST": 
        if request.POST['first_name'] != '' : 
            fname = request.POST['first_name']
        if  request.POST['last_name'] != '' :    
            lname = request.POST['last_name']
        if  request.POST['email'] != '' :       
            email = request.POST['email']
        if  request.POST['age'] != '' and request.POST['age'].isnumeric(): 
                 age = int(request.POST['age'])
         
        edit_user = Users.objects.get(id=id)
        edit_user.first_name = fname 
        edit_user.last_name = lname
        edit_user.age = age
        edit_user.email_address =email 
        edit_user.save()         
       
    return redirect("/")     