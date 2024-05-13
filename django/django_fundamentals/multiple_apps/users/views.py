from django.shortcuts import render, HttpResponse,redirect

# Create your views here.


def root(req):
    return redirect("bolgs_app:index")
def index(req):
    return HttpResponse("placeholder to later display all the list of users")
    
def register(req):
    return HttpResponse("placeholder for users to create a new user record")
    
def login(req):
    return HttpResponse("placeholder for users to log in") 
def new(req):
    return redirect("users_app:register")
    







