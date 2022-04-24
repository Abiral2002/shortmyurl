from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
# from flask_wtf import wtforms
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError

app = Flask(__name__)
db = SQLAlchemy(app)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///database.db'
app.config["SECRET_KEY"] = 'aN&^Q7&47C2Qwv9kv2rCvzcPC5C982Sn$YFg%CW$'

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.column(db.String(30))
    password = db.column(db.String(30))

@app.route('/')
def index():
    return render_template('index.html', name='index')

@app.route('/login')
def login():
    return render_template('login.html', name='login')

@app.route('/reset')
def reset():
    return render_template('reset.html', name='reset')

@app.route('/register')
def register():
    return render_template('register.html', name='register')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', name='dashboard')

@app.route('/about')
def about():
    return render_template('about.html', name='about')

@app.route('/contact')
def contact():
    return render_template('contact.html', name='contact')

if __name__ == '__main__':
    app.run(debug=True, port=8000)