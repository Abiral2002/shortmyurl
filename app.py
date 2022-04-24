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


if __name__ == '__main__':
    app.run(debug=True, port=8000)