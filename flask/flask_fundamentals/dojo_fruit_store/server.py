from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
# [('strawberry', '0'), ('raspberry', '0'), ('apple', '0'), ('first_name', 'mustafa'), ('last_name', 'taha'), ('student_id', '125')]
    straw = int(request.form['strawberry'] )
    rasp  = int(request.form['raspberry'])
    apple = int(request.form['apple'])
    count=straw+rasp+apple
    fname = request.form['first_name']
    lname = request.form['last_name']
    id= request.form['student_id']
    return render_template("checkout.html",straw=straw,rasp=rasp,
                           apple=apple,fname=fname,lname=lname,id=id,count=count)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    