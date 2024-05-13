from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
def index(req):
    return HttpResponse("placeholder to display all the surveys created")


def new(req):
    return HttpResponse("placeholder for users to add a new survey")