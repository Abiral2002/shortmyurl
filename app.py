from enum import unique
from datetime import datetime
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import string
from random import choices


app = Flask(__name__)
db = SQLAlchemy(app)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///database.db'
app.config["SECRET_KEY"] = 'aN&^Q7&47C2Qwv9kv2rCvzcPC5C982Sn$YFg%CW$'

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.column(db.String(30))
    password = db.column(db.String(30))

class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(600))
    short_url = db.Column(db.String(30), unique=True)
    visits = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.short_url = self.generate_short_link()

    def generate_short_link(self):
        character = string.digits + string.ascii_letters
        short_url = ''.join(choices(character, k=10))

        link = self.query.filter_by(short_url=short_url).first()

        if link:
            return self.generate_short_link()
        
        return short_url

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