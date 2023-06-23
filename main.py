from flask import Flask,render_template,flash,redirect
from flask import request

import rankPredictor as rp
app = Flask(__name__)
app.config['SECRET_KEY'] ='24ccf7efc0cae54f1bf927e7f59ee5e8f2' #unique secret key created by import os os.urandom(17),hex()

#connecting to sql
from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///site.db'#create sql database in the same directory 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)#sqlalchemy instance creation
# model created in model.py file
from __main__ import db
class User(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(20),unique=True,nullable=False)
    email=db.Column(db.String(120),unique=True,nullable=False)
    img_file=db.Column(db.String(120),nullable=False,default="default.jpg")  #hash the image to string20
    password=db.Column(db.String(60),nullable=False)#hashed string of 60 character
    
    def __repr__(self):#used to specify how our object is going to be printed-> print(object)
        return f"user('{self.username}','{self.email}','{self.img_file}')"

# from model import User

#router handling
@app.route("/", methods=['GET', 'POST'])
def hello_world():
    name="Arjun Kumar Soni"
    return render_template('index.html',name=name)

@app.route("/features", methods=['GET', 'POST'])

def hello_world2():
    if request.method == 'POST':
        institute=[]
        x=int(request.form['rank'])
        y=(request.form['name'])
        name=rp.predict(x)
        for j in name:
            j=j.to_dict()
            n = 0
            for i in j["S.NO"].values():
                n = i
            institute.append({"name": (j["INSTITUTE NAME"][n]),
                    "branch": (j["BRANCH"][n]),
                    "type":j["INSTITUTE TYPE"][n],
                    "open":j["JEE OPENING RANK"][n],
                    "close":j["JEE CLOSING RANK"][n],
                    "category":j["ALLOTTED CATEGORY"][n]
                    })
        return render_template('predictor.html',institute=institute,y=y)#variables are passed to html like the
    else:
        return render_template('index1.html')

@app.route("/about", methods=['GET', 'POST'])
def hello_world3():
    name="Arjun Kumar Soni"
    flash(f'hi this is from {name}','success')#flash messages are handled in html.created only single time.
    return render_template('about.html')

app.run(debug=True)