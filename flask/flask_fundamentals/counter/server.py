from flask import Flask,render_template,redirect,request,session



app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route("/")
def show():
    print(session)
    if 'count' in session :
        if 'from_function' not in session or session['from_function'] == False : 
            session['count'] = session['count'] + 1
    else: 
        session['count'] = 1
    session['from_function'] = False        
    return render_template("index.html")

@app.route("/increamt",methods=['POST'])
def make_count():
    #print(request.form)
    # if 'count' in session:
    session['count'] = session['count'] + 2
    session["from_function"]=True
    # else: 
    #     session['count'] = 1 
    return redirect("/")     

@app.route("/destroy_session",methods=['POST'])
def reset_count():
    session.clear()		# clears all keys
    #session.pop('count')		# clears a specific key
    session["from_function"]=True
    return redirect("/")


@app.route("/increamt_by_n",methods=['POST'])
def makei_count():
    #print(request.form)
    # if 'count' in session:
    if request.form['n'].isnumeric():
        session['n'] = int(request.form['n']) 
        if session['n'] >= 0 :
            session['count'] = session['count'] + session['n']
    session["from_function"]=True        

    # else: 
    #     session['count'] = 1 
    return redirect("/")   


if __name__=="__main__":
    app.run(debug=True)