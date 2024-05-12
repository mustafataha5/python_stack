from django.shortcuts import render,HttpResponse,redirect

# Create your views here.


def index(req):
    print(req.POST)  
    return render(req,'index.html')
            
def some_fun(req):
    if req.method == 'GET':
        print("A GET request is being made to this route")
        return render(req,'request.html')
    if req.method == 'POST' :  
         print("A POST request is being made to this route")
         print(req.POST)
         return redirect('/')