from django.shortcuts import render,redirect,HttpResponse
from .models import User,Book
import bcrypt
from django.contrib import messages
# Create your views here.
def index(request):
    if 'userID' in request.session:
        messages.success(request,"Welcome back from last session")
        return redirect('book:main_page')
    
    return redirect('book:reg&login')

def registeration_and_login(request):
    return render(request,'index.html')       


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
        hash_password = bcrypt.hashpw(request.POST['password'].encode(),bcrypt.gensalt()).decode() 
        user = User.objects.create(first_name=user_fname,last_name=user_lname,email=email,password=hash_password)    
      
        
        request.session['userID'] =user.id 
        messages.success(request,"Successful registeration ")
        return redirect('book:main_page')    

def main_page(request):
    if not 'userID' in request.session:
        messages.warning(request,'You need to regiester or login',extra_tags='invalid_accuess')
        return redirect('/')
    data={
        "user":User.objects.get(id=request.session['userID']),
        'books':Book.objects.all(),
    }
    
    return render(request,'main_page.html',data)

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
        return redirect('book:main_page')  

def logout(request):
    request.session.clear()
    return redirect("/")
    


def add_book(request): 
    if request.method == 'POST' : 
        errors = Book.objects.book_validation(request.POST)
         
        if len(errors) > 0 : 
            for key,val in errors.items(): 
                messages.error(request,val,extra_tags=key)
            return redirect('book:main_page')  
        
        userID = request.session['userID']
        user = User.objects.get(id=userID)
        book_title = request.POST['title']
        book_description = request.POST['description']
        book = Book.objects.create(title=book_title,desc=book_description,uploaded_by=user)
        book.users_who_like.add(user)
        
    return redirect('book:main_page')

def add_faverite_book(request):
    if request.method == 'POST': 
        bookID = request.POST['bookID']
        userID = request.session['userID']
        book = Book.objects.get(id=bookID)
        user = User.objects.get(id=userID)
        book.users_who_like.add(user)
        if "frombookID" in request.POST : 
            return redirect(f'/book/{bookID}')    
    return redirect('book:main_page')


def book(request,bookID):
    userID = request.session['userID']
    request.session['bookID'] = bookID
    user = User.objects.get(id=userID)
    book = Book.objects.get(id=bookID)
    data={
        "user":user , 
        "book":book , 
    }
    if (user == book.uploaded_by):
        return  render(request,'edit_book.html',data)
    else : 
        return render(request,'show_book.html',data)




def edit_book(request,bookID): 
    if request.method == 'POST' : 
        errors = Book.objects.book_validation(request.POST)
         
        if len(errors) > 0 : 
            for key,val in errors.items(): 
                messages.error(request,val,extra_tags=key)
            redirect(f'/book/{bookID}')  
        
        book = Book.objects.get(id=bookID)
        book_title = request.POST['title']
        book_description = request.POST['description']
        book.title = book_title
        book.desc = book_description 
        book.save()
    return redirect('book:main_page')

def delete_book(request,bookID): 
    if 'userID' in request.session and bookID == request.session['bookID'] :
        request.session['bookID'] = -1  
        book = Book.objects.get(id=bookID)
        book.delete()
    return redirect('book:main_page')


def delete_user_from_book (request,bookID): 
    if request.method == 'POST' : 
        book = Book.objects.get(id=bookID)
        userID = int(request.POST['user_who_like'])
        user= User.objects.get(id=userID)
        book.users_who_like.remove(user)
    
    return redirect(f'/book/{bookID}')