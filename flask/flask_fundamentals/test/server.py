from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def hellow():
    return "<h1> Mustafa taha</h1>"
@app.route("/<name>")
def hello(name):
    return f"Hello , {escape(name)}!"
@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'
# @app.route("/<name>/<id>")
# def hello2(name,id):
#     return f"Hello , {id}!"


if( __name__=="__main__"):
    app.run(debug=True)