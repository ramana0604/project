import time     

from flask import Flask, render_template, request   #flask is used for integrate a html and python code.

app = Flask(__name__)   #Initalize the flask.


@app.route('/')
def entry():
    return render_template('home.html')

@app.route('/home') 
def home():
    return render_template('home.html')


@app.route('/getdata', methods=['POST','GET'])
def submit():
    name= request.form['name']
    db = request.form['DOB']
    event = request.form['event']
    email = request.form['email']
    sender = request.form['send']
   
    
    x = name        # This is used for  store the data in the file 
    y = db
    z = event
    v=email
    s =sender
    f = open("member.txt","a+")
    f.write(y+' ')
    f.write(z+' ')
    f.write(x+' ')
    f.write(v+' ')
    f.write(s+' ')
    f.write('\n')
    f.close()
    print("value writted")

    return render_template('index.html',)

if __name__=="__main__":
    app.run(debug=True)


    #The server can be run 24/7 to check the birthday and anniversary date for wishing.
    #server.py  is used for that work.