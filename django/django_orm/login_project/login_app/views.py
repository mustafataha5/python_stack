from django.shortcuts import render,redirect,HttpResponse
from .models import User
import bcrypt
from django.contrib import messages
# Create your views here.
def index(request):
    if 'userID' in request.session:
        messages.success(request,"Welcome back from last session")
        return redirect('/success')
        
    return render(request,'index.html')


def create_user(request):
    if request.method == "POST": 
        errors = User.objects.basic_validation(request.POST)
        if len(errors) > 0 : 
            for key,val in errors.items(): 
                messages.error(request,val,extra_tags=key)
            return redirect('/') 
        
        user_fname = request.POST['first_name'] 
        user_lname = request.POST['last_name']
        email =  request.POST['email'] 
        hash_password = bcrypt.hashpw(request.POST['password'].encode(),bcrypt.gensalt()).decode() 
        user = User.objects.create(first_name=user_fname,last_name=user_lname,email=email,password=hash_password)    
      
        
        request.session['userID'] =user.id 
        messages.success(request,"Successful registeration ")
        return redirect('/success')    

def success(request):
    if not 'userID' in request.session:
        messages.warning(request,'You need to regiester or login',extra_tags='invalid_accuess')
        return redirect('/')
    data={
        "user":User.objects.get(id=request.session['userID'])
    }
    
    return render(request,'success.html',data)

def login_user(request):
    if request.method == "POST": 
        errors = User.objects.login_validation(request.POST)
        if len(errors) > 0 : 
            for key,val in errors.items(): 
                messages.error(request,val,extra_tags=key)
            return redirect('/') 
        user = User.objects.get(email=request.POST['email'])    
        request.session['userID'] = user.id
        messages.success(request,"Successful login ")
        return redirect('/success')  

def logout(request):
    request.session.clear()
    return redirect("/")
    
