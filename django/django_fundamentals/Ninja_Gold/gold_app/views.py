from django.shortcuts import render,redirect
import random 
from datetime import datetime
# Create your views here.
def index(request):
    return render(request,'start.html')
    
def gold (request):
    if not 'counter' in request.session : 
        request.session['counter'] = 0
        request.session['message'] = ""
        request.session['num_of_gold'] = 0
        request.session['win'] = False
       
        
    if  request.session['total_gold'] <= request.session['num_of_gold']:
            request.session['win'] = True 
            return render(request,'show.html')
    if  request.session['counter'] >= request.session['total_step']: 
            return render(request,'show.html')
     
    return render(request,'index.html')


def process(request,from_which):
  
    if request.method == "GET": #request.method == "POST":
        gold_dict = {
            "farm":  random.randint(10,20),
            "cave":  random.randint(10,20),
            "house": random.randint(10,20),
            "quest": random.randint(-50,50),            
        }
        now = datetime.now()

        current_time = now.strftime("%B %d %Y  %H:%M:%S")
        num_of_gold = gold_dict[from_which] 
        request.session['counter'] = request.session['counter'] +1 
        request.session['num_of_gold'] =  request.session['num_of_gold'] + num_of_gold
        if  num_of_gold > 0 : 
            new_message = "<li class='green'>You enterd a "+from_which+"and earned "+str(num_of_gold)+" gold. "+str(current_time)+"</li>"
        else:    
            new_message = "<li class='red'>You failed a "+from_which+"and lost "+str(abs(num_of_gold))+" gold. Ouch "+str(current_time)+"</li>"
        request.session['message'] = new_message+ request.session['message']
    return redirect("/gold") 

def reset(request):
    if 'counter' in request.session:
        request.session.pop('counter')
    return redirect("/gold")   


def set_attr(request):
    if request.method == "POST" : 
        if request.POST['user_total_gold'] == '' : 
            total_gold = 100 
        else : 
            total_gold = int(request.POST['user_total_gold'])
        
        if  request.POST['user_step_number'] == ''  :    
            total_setp = 10
        else:
            total_setp= int(request.POST['user_step_number'])
        
        request.session['total_gold'] = total_gold
        request.session['total_step'] = total_setp
        
    return redirect("/reset")




