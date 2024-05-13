from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
def index(req): 
    return HttpResponse("placeholder to later display a list of all blogs")
    
def new(req): 
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(req):
    return redirect("bolgs_app:index")

def show(req,number):
    return HttpResponse(f"placeholder to display blog number: {number}")

def edit(req,number):
    return HttpResponse(f"placeholder to edit blog {number}")

def destroy(req,number):
    return redirect("bolgs_app:index")
