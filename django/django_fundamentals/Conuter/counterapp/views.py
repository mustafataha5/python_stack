from django.shortcuts import render,redirect

# Create your views here.
def index(request): 
    
    if not 'user_count' in request.session : 
        request.session['user_count'] = 1 
        request.session['count'] = 1  
        request.session['from_fun'] = False 
    elif 'from_fun' in  request.session and not  request.session['from_fun']  : 
        request.session['user_count'] += 1  
        request.session['count'] += 1
    request.session['from_fun'] = False   
            
    return render(request,'index.html')


def destroy_session(request):
    request.session.pop("user_count") 
    request.session.pop("count") 
    return redirect('/')

def add_two(request):
    request.session['count'] += 2 
    request.session['from_fun'] = True
    return redirect('/')

def add_n(request):
    if request.method == 'POST' : 
        n = request.POST['n']
        if n.isnumeric() and int(n) >= 1: 
            request.session['count'] += int(n) 
            request.session['from_fun'] = True
    return redirect('/')



