from django.shortcuts import render,redirect
from  django.contrib import messages
from .models import User,Message,Comment
import bcrypt
# Create your views here.

def index(request):
    if 'userID' in request.session:
        messages.success(request,"Welcome back from last session")
        return redirect('/wall')
        
    return render(request,'index.html')

def main_wall(request):
    if not 'userID' in request.session:
        #messages.warning(request,'You need to regiester or login',extra_tags='invalid_accuess')
        return redirect('/')
    data={
        "user":User.objects.get(id=request.session['userID']),
        "posts":Message.objects.all().order_by('-updated_at'),
    } 
    return render(request,'wall_page.html',data)


def create_user(request):
    if request.method == "POST": 
        errors = User.objects.basic_validation(request.POST)
        if len(errors) > 0 : 
            for key,val in errors.items(): 
                messages.error(request,val,extra_tags=key)
            return redirect('/') 
        
        user_fname = request.POST['first_name'].capitalize() 
        user_lname = request.POST['last_name'].capitalize()
        email =  request.POST['email'] 
        birthday = request.POST['birthday']
        hash_password = bcrypt.hashpw(request.POST['password'].encode(),bcrypt.gensalt()).decode() 
        user = User.objects.create(first_name=user_fname,last_name=user_lname,email=email,password=hash_password,birthday=birthday)    
      
        
        request.session['userID'] =user.id 
        #messages.success(request,"Successful registeration ")
        return redirect('wall_app:main_page')    


def login_user(request):
    if request.method == "POST": 
        errors = User.objects.login_validation(request.POST)
        if len(errors) > 0 : 
            for key,val in errors.items(): 
                messages.error(request,val,extra_tags=key)
            return redirect('/') 
        user = User.objects.get(email=request.POST['email'])    
        request.session['userID'] = user.id
        #messages.success(request,"Successful login ")
        return redirect('wall_app:main_page')

    
def logout(request):
    request.session.clear()
    return redirect('wall_app:index')


def add_post(request):
    if request.method == 'POST': 
        errors = Message.objects.post_validation(request.POST)
        user =User.objects.get(id=request.session['userID']) # for testing
        if len(errors) > 0 : 
            for key,val in errors.items(): 
                messages.error(request,val,extra_tags=key)
        else: 
            Message.objects.create(message=request.POST['post_message'],user=user)       
    return redirect("wall_app:main_page")


def add_comment(request,postID):
    if request.method == 'POST': 
        errors = Comment.objects.comment_validation(request.POST,postID,request.session['userID'])
        if len(errors) > 0 : 
            for key,val in errors.items():
                messages.error(request,val,key)
            return redirect("wall_app:main_page")    
        post = Message.objects.get(id=postID) 
        user = User.objects.get(id=request.session['userID'])       
        Comment.objects.create(comment_message=request.POST['comment_message'],user=user,message=post)
                
    
    return redirect('wall_app:main_page')


def delete_post(request,postID):
    if Message.objects.can_delete(postID) :
        post = Message.objects.get(id=postID)
        post.delete()    
    return redirect('wall_app:main_page')




