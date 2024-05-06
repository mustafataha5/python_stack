from flask import Flask,render_template,request,make_response   # type: ignore




app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html',name="world",list=[],student=[])

@app.route("/<name>")
def hello_name(name):
    return render_template('index.html',name=name,list=[],student=[])

@app.route("/list")
def show_list():
    list = [1 , 2 , 3]
    student = [
        {'name':'mustafa','score':90},
        {'name':'taha','score':85},
        {'name':"yousef",'score':92}
    ]
    return render_template('index.html',name="list",list=list,student=student)

@app.route('/setcookie', methods = ['POST', 'GET']) 
def setcookie(): 
    if request.method == 'POST': 
        user = request.form['nm'] 
        print("*"*30,"",user)
        resp =make_response(render_template('cookie.html')) 
        resp.set_cookie('userID', user) 
        return resp 

@app.route('/getcookie') 
def getcookie(): 
    name = request.cookies.get('userID') 
    return '<h1>welcome '+name+'</h1>'


if __name__=="__main__":
    app.run(debug=True)