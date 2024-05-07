from flask import Flask,render_template,redirect,request,session



app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route("/")
def show():
    if 'count' in session: 
        session['count'] = session['count'] + 1
    else: 
        session['count'] = 1     
    return render_template("index.html")

@app.route("/increamt",methods=['POST'])
def make_count():
    #print(request.form)
    # if 'count' in session: 
    session['count'] = session['count'] + 1
    # else: 
    #     session['count'] = 1 
    return redirect("/")     

@app.route("/destroy_session",methods=['POST'])
def reset_count():
    #session.clear()		# clears all keys
    session.pop('count')		# clears a specific key
    return redirect("/")





if __name__=="__main__":
    app.run(debug=True)