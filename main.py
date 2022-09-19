from flask import Flask, redirect,render_template,request
app= Flask(__name__)

@app.route('/')
def index():
    return "hola mundo"

@app.route('/login')
def login():
    return render_template('login.html')

if __name__=='__main__':
    app.run(debug=True)
    #app.run(debug=True,host = '127.0.0.1', port = '5001')
    #app.run(debug=True,host = '0.0.0.0', port = '80')
