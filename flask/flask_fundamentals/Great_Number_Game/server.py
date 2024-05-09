from flask import Flask,request,redirect,session,render_template 
import random 
from winner import Winner # class we bluid 



app = Flask(__name__)
app.secret_key = "you>password@here$#@"

winner = [] # wiiner list 

@app.route("/")
def index():
    if not 'number_to_guess' in session or ('win' in session and session['win']==True): 
        session['number_to_guess'] = random.randint(1,100)
    if 'guess_count' in session and session['guess_count'] >= 5 : 
        session['can_guess']=False
    else:
        session['can_guess'] = True  
      
    print(session)
    print("*"*15,len(winner))    
    return render_template('index.html',length_of_list=len(winner))

@app.route("/guess",methods=['POST'])
def guess():
    #print(request.form)
    if (request.form['user_guess'].isnumeric() ):
 
        if not  'guess_count' in session:
            session['guess_count'] = 1
        else:
            session['guess_count'] = session['guess_count'] + 1
 
        guess_number = int(request.form['user_guess'] ) 
        session['user_guess'] = guess_number

        if guess_number > session['number_to_guess']:
            session['low'] = False
            session['win'] = False
        elif guess_number < session['number_to_guess']:
            session['low'] = True
            session['win'] = False
        else: 
            session['win'] = True

    return redirect("/")

@app.route("/save_winner",methods=['POST'])
def save_winner():
    newWinner = Winner(request.form['winner_name'],session['guess_count'])
    winner.append(newWinner)
    if not 'winner' in session :  
         session['winner'] = []  
    else: 
        session['winner'].append(newWinner)

    print("*"*30,len(session['winner']))    
    return redirect('/play_again')

@app.route("/play_again")
def play_agian():
    #session.clear()
    if 'guess_count' in session:
        session.pop('guess_count')
    if  'number_to_guess' in session:  
        session.pop('number_to_guess')
    if 'can_guess' in session:
        session.pop('can_guess')
    if 'low' in session:
        session.pop('low')   
    if 'win' in session:
        session.pop('win')    

    return redirect("/")

@app.route("/show")
def show_winner():
    return render_template("show.html",winner=winner)

if __name__=="__main__":
    app.run(debug=True)