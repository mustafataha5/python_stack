from django.shortcuts import render,HttpResponse,redirect

from .models import Dojo,Ninja

# Create your views here.

def index(req): 
    data ={
        "Dojos": Dojo.objects.all(),
    }
    return  render(req,'index.html',data)


def add_dojo(req):
    if req.method== "POST": 
        if req.POST["name"] != '' and req.POST["city"] != '' and req.POST["state"] != '' : 
            dojo_name = req.POST['name']
            dojo_city = req.POST['city']
            dojo_state = req.POST['state']
            #dojo_desc = req.POST('desc') 
            Dojo.objects.create(name=dojo_name,city=dojo_city,state=dojo_state)
            
    return  redirect("/")       
            
def add_ninja(req):
    if req.method== "POST": 
        if req.POST["first_name"] != '' and req.POST["last_name"] != '' and req.POST["select_dojo"] != '' : 
            first_name = req.POST['first_name']
            last_name = req.POST['last_name']
            dojo_id = int(req.POST['select_dojo'])
            select_dojo = Dojo.objects.get(id=dojo_id)
            #dojo_desc = req.POST('desc') 
            Ninja.objects.create(first_name=first_name,last_name=last_name,dojo=select_dojo)
            
    return  redirect("/")             
            
            
            
            
            
            
            
            
            
            