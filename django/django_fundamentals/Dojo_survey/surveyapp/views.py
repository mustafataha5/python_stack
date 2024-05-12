from django.shortcuts import render

# Create your views here.
def index(req):
    return render(req,'index.html')


def result(req): 
    if req.method == "POST":
        data = {
            "name" : req.POST['Name'] , 
            "lang" : req.POST['lang'],
            "locat": req.POST["location"],
            "gender": req.POST['gender'],
            "fruits" : req.POST.getlist('fruits') , 
            "comment" : req.POST['comment'],
        }
        return render(req,'result.html',data)
