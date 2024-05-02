from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def start():
    return "<h1 style='margin: 50px auto;text-align:center;'>Welecome, enter localhost:5000/play/num/color</h1>"
@app.route("/play/")
def play():
    return render_template("index.html",x=3,color="#9fc5f8")

@app.route("/play/<int:x>")
def play_x(x):
    return render_template("index.html",x=x,color="#9fc5f8")

@app.route("/play/<int:x>/<color>")
def play_x_color(x,color):
    return render_template("index.html",x=x,color=color)


if __name__=="__main__" : 
    app.run(debug=True)