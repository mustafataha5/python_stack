from flask import Flask, render_template

app = Flask(__name__)



@app.route("/")
def defalut():
    return render_template("index.html",x=8,y=8,color1="sandybrown",color2="black")

@app.route("/<int:x>")
def control_x(x):
    return render_template("index.html",x=x,y=8,color1="rgb(108, 175, 31)",color2="rgb(33, 119, 153)")

@app.route("/<int:x>/<int:y>")
def control_xy(y,x):
    return render_template("index.html",x=x,y=y,color1="rgb(108, 175, 31)",color2="rgb(33, 119, 153)")
@app.route("/<int:x>/<int:y>/<string:color1>/<string:color2>")
def control_xy_color(y,x,color1,color2):
    return render_template("index.html",x=x,y=y,color1=color1,color2=color2)


if __name__=="__main__":
    app.run(debug=True)
