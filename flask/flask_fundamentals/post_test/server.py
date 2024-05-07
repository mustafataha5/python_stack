from flask import Flask,render_template ,request,redirect,session




app = Flask(__name__)
app.secret_key = "keep me secret 2024 !@#"

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/process",methods=['POST'])
def process_users():
    print("in process users function")
    print(request.form['name'])
    session['user_name'] = request.form['name']
    session['user_email'] = request.form['email']
    return redirect("/show")
@app.route("/show")
def show_user():

    return render_template('show.html',name=session['user_name'],email=session['user_email'])


if __name__=="__main__":
    app.run(debug=True)