from django.shortcuts import render,redirect

# Create your views here.

from time import gmtime, strftime
    
def index(request):
    context = {
        "time": strftime("%H:%M %p", gmtime()),
        "date": strftime("%B  %d , %Y", gmtime()),
    }
    return render(request,'index.html', context)


def display(req):
    return redirect("/")

def display2(req):
    return render(req,"index2.html")



