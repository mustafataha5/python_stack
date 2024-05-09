from flask import Flask, redirect,request,session,render_template
import random
import time 


app = Flask(__name__)
app.secret_key ="any_password@_here"


@app.route("/")
def index():
    if not 'total_gold' in session : 
        session['total_gold'] = 0 
        session['message'] = ""
        session['counter']=0
        session['win'] = False
        session['game_finish'] = False
        
    return render_template("index.html")



@app.route("/process_money",methods=['POST'])
def process():
    
    dict = {
        'farm': random.randint(10,20),
        'cave': random.randint(5,10),
        'house':random.randint(2,5),
        'casino': random.randint(-50,50)
    }
    print('*************',session)
    from_input = request.form['building']
    gold = dict[from_input]
    named_tuple = time.localtime() # get struct_time
    time_string = time.strftime("%Y/%m/%d, %H:%M:%S %p", named_tuple)    
    
    if gold >= 0 :
        session['message'] = "<li class='green'>Earn "+str(gold)+" golds from "+from_input+"!( "+time_string+")</li>"+session['message']      
    else: 
        session['message'] = "<li class='red'>Enter casino and lost "+str(gold)+" golds ... Ouch!!!... ( "+time_string+")</li>"+session['message']    
    
    session['total_gold'] =  session['total_gold'] + gold 
    session['counter'] = session['counter']+1
    
    if session['total_gold'] >= 100 and session['counter'] <= 15: #500:
        session['game_finish'] = True
        session['win'] = True
    elif  session['counter'] > 15:
        session['game_finish'] = True
        session['win'] = False    
        
    
    return redirect("/")

@app.route("/reset")
def destroy_session():
    session.clear()
    return redirect("/")    

if __name__=="__main__":
    app.run(debug=True)


