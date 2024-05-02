from  flask import Flask ,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',username="taha",time=5)
# import statements, maybe some other routes

@app.route('/success')
def success():
  return "success"

# app.run(debug=True) should be the very last statement!
@app.route('/hello/<name>')
def hello(name):
    print(name)
    return "Hello ,"+name
@app.route('/user/<username>/<id>')
def hello_user(username,id):
    print(username)
    print(id)
    return "username: "+username+" id: "+id


if __name__ == "__main__":
    app.run(debug=True)
