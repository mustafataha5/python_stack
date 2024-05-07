from flask import Flask, render_template, request, redirect


app = Flask(__name__)



@app.route("/")
def form():
    return render_template('index.html')

@app.route("/result",methods=['POST'])
def result():
    print(request.form)

    return render_template('result.html',name=request.form['Name'],locat=request.form['location'],
                            lang=request.form['lang'] ,comment=request.form['comment'])


if __name__=="__main__":
    app.run(debug=True)