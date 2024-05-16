from django.shortcuts import render,redirect
from .models import Author,Book
def index(request):
    data = {
        "books": Book.objects.all() , 
    }
    return render(request,'index.html',data)

def index_books(request):
    return redirect('/')

def add_book(req):
    if req.method == 'POST':
        if req.POST['add_title'] != ''  : 
            #print(req.POST)
            book_title = req.POST['add_title'] 
            book = Book.objects.create(title=book_title)
            if req.POST.get('add_book_decs') != "" :
                book_desc = req.POST.get('add_book_decs')
                book.desc = book_desc
                book.save()
    
    return  redirect('/')       

def show_book(req,id):
    if req.method == 'GET' : 
        book = Book.objects.get(id=id)
        authors = book.authors.all()
        
        data= {
            "book":Book.objects.get(id=id),
            "exclude_authors": Author.objects.exclude(id__in=authors.values('id'))
        }
        
        return render(req,"show_book.html",data)            
    
    
def add_author_to_book(req,id): 
    
    if req.method == 'POST' : 
        if req.POST['select_author'] != '': 
            get_author_id = int(req.POST['select_author'])
            add_author = Author.objects.get(id=get_author_id)
            book = Book.objects.get(id=id)
            book.authors.add(add_author)
                    
    return redirect(f"/book/{id}")    

def index_authors(req): 
    data = {
        "authors":Author.objects.all()
    }    
    return render(req,'authors.html',data)


def add_author(req): 
    if req.method == 'POST' : 
        if req.POST['add_first_name'] != '' and req.POST['add_last_name'] != '':
            author_fname = req.POST['add_first_name']
            author_lname = req.POST['add_last_name']
            new_author=Author.objects.create(first_name=author_fname,last_name=author_lname)
            if req.POST['add_notes']!='':
                new_author.notes = req.POST['add_notes']
                new_author.save()
    return redirect('/authors')


def show_author(req,id):
    
    author= Author.objects.get(id=id)
    author_books = author.books.all()
    ex_books = Book.objects.exclude(id__in=author_books.values('id'))
    
    data = {
        "author": author, 
        "ex_books":ex_books,
    }
    
    return render(req,'show_author.html',data)


def add_book_to_author(req,id): 
    if req.method=="POST" : 
         if req.POST['select_book'] != '': 
            get_book_id = int(req.POST['select_book'])
            add_book = Book.objects.get(id=get_book_id)
            author = Author.objects.get(id=id)
            author.books.add(add_book)
                    
    return redirect(f"/author/{id}")    