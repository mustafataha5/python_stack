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


