from django.shortcuts import render,redirect
import random 

# class Winner: 
#     def __init__(self,name,count) -> None:
#         self.name = name 
#         self.count = count 

# Create your views here.
def index (request):
    if not 'random_number' in request.session : 
        request.session['random_number'] = random.randint(1,100)
        request.session['counter'] = 0
        request.session['win'] = False
        
    if not  'winner_list' in request.session : 
        request.session['winner_list'] = []    
        request.session['in_list'] = False
    print(request.session['winner_list'][0])        
    return render(request,"index.html")




def guess(request):
    
    if request.method == "POST" : 
        guess_number = request.POST['user_guess']
        if(guess_number.isnumeric ()):
            user_number  = int(guess_number)
            request.session['counter'] += 1  
            if user_number > request.session['random_number']: 
                request.session['low'] = False
                request.session['win'] = False 
            elif user_number < request.session['random_number']: 
                 request.session['low'] = True
                 request.session['win'] = False
            elif user_number == request.session['random_number']: 
                request.session['win'] = True     
                     
    return redirect("/")

import json
def play_again(request): 
    
    request.session.pop("random_number")
    request.session.pop("counter")
    request.session.pop("win")
    return redirect("/")



def save_winner(request) : 
    
    if request.method == "POST": 
        
        winner_name = request.POST['winner_name']    
        #newWinner = winner_name,request.session['counter'])
        # print(newWinner.name)
        # newObj = json.dumps(newWinner)
        data = {
            "name": winner_name, 
            "count": request.session['counter'],
        }
        request.session['winner_list'].append(data)
        request.session['in_list'] = True
        
        request.session.save()    
    
    return redirect("/play_again")

def show(request): 
    
    return render(request,'show.html')