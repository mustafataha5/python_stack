

from flask import Flask 


app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello world!"

@app.route("/dojo")
def dojo():
    return "Dojo!"
@app.route("/say/<name>")
def Hi(name):
    return "HI! "+name

@app.route("/repeat/<int:num>/<name>")
def repeate(num,name):
    return (" "+name)*num

@app.route('/users/', defaults={'path': ""})
@app.route('/<path:path>')
def sorry(path):
    return "Sorry , No response. Try again !!! " +str(path)


if __name__=="__main__" : 
    app.run(debug=True)