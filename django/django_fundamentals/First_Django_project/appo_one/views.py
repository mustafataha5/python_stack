from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse
# Create your views here.



def root (req):
    return redirect('/blogs')


def index(req):
    return HttpResponse("placeholder to later display a list of all blogs")


def new(req):
    return HttpResponse("placeholder to display a new form to create a new blog" )


def create(req):
    return redirect('/')

def show(req,number):
    return HttpResponse(f"placeholder to display blog number: {number}")


def edit(req,number):
    return HttpResponse(f"placeholder to edit blog {number}" )


def destroy(req,number):
    return redirect('/blogs')


def send_json(req):
    return JsonResponse({
                            "title":"My first blog",
                            "content": "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Amet, a vitae eum quibusdam.",
                        })