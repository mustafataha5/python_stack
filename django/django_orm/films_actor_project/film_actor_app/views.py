from django.shortcuts import render ,redirect,HttpResponse
from .models import Actor,Movie,Category,Language
# Create your views here.

def index(request): 
    # data = {
    #     "movies" : Movie.objects.all(),
    #     "actors" : Actor.objects.all(),
    #     "catrgory" : Category.objects.all() ,
    # }
    # return render(request,'index.html',data)
    return redirect('/movies')

def index2(request): 
    data = {
        "movies" : Movie.objects.all(),
    }
    return render(request,'index2.html',data)

def show_movie(request,id):
    movie = Movie.objects.get(id=id)
    data={
        "movie":movie , 
    }
    return render(request,"show_movie.html",data)


def show_all_actors(request):
    data = {
        "actors":Actor.objects.all(), 
    }
    return render(request,'show_actors.html',data)



