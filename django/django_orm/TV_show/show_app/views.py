from django.shortcuts import render,redirect
from .models import Show
# Create your views here.



def index(request):
    
    return redirect('/shows')

def show_all(request):
    data= {
        "shows":Show.objects.all(),
    }
    return render(request,'index.html',data)


def show_new (request):
    return render(request,'show_new.html')



def create_show(request):
    if request.method == 'POST': 
        title = request.POST['title']
        description = request.POST['description']
        release_date = request.POST['release_date'] 
        newtork = request.POST['network']
        show = Show.objects.create(title=title,description=description,network=newtork,release_date=release_date)
    
    return redirect(f'/shows/{show.id}')


def show_by_id(request,id):
    
    data={
        "show":Show.objects.get(id=id)
    }
    return render(request,"show_id.html",data)


def destroy_show(request,id):
    
    del_show = Show.objects.get(id=id)
    del_show.delete()
    
    return redirect("/shows")

def edit_show(request,id):
    data = {
        "show" : Show.objects.get(id=id)
    }
    return render(request,"show_id_edit.html",data)

def update_show(request,id):
    if request.method == 'POST' :
        
        update_show =  Show.objects.get(id=id)
        update_show.title = request.POST['title']
        update_show.release_date = request.POST['release_date']
        update_show.description = request.POST['description']  
        update_show.network = request.POST['network']
        update_show.save()  
    return redirect(f"/shows/{id}")