from unicodedata import name
from flask import Flask, render_template

app = Flask(__name__)

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
@login_required
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