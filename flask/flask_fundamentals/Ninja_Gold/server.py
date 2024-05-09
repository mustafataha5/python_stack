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
    return render_template("index.html")



@app.route("/process_money",methods=['POST'])
def process():
    print(request.form['building'])
    from_input = request.form['building']
    gold = 0
    if from_input == "farm": 
        
       gold = random.randint(10,20)
    elif from_input == "cave": 
        gold = random.randint(5,10)
    elif from_input == "house":
       gold = random.randint(2,5)
    elif from_input == "casino": 
        gold =random.randint(-50,50)
    
    
    named_tuple = time.localtime() # get struct_time
    time_string = time.strftime("%Y/%m/%d, %H:%M:%S %p", named_tuple)    
    
    if gold >= 0 :
        session['message'] = "<li class='green'>Earn "+str(gold)+" golds from "+from_input+"!( "+time_string+")</li>"+session['message']      
    else: 
        session['message'] = "<li class='red'>Enter casino and lost "+str(gold)+" golds ... Ouch!!!... ( "+time_string+")</li>"+session['message']    
    session['total_gold'] =  session['total_gold'] + gold  
    return redirect("/")

@app.route("/reset")
def destroy_session():
    session.clear()
    return redirect("/")    

if __name__=="__main__":
    app.run(debug=True)


