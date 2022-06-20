from flask import Flask, redirect,render_template, session, redirect
from functools import wraps
import pymongo

app = Flask(__name__)
app.secret_key = b'\xb1\x16\xe7\xfe\xf8\x1d\x1b\x9b5\xe2\xf6\x9f`\t\x96)'
app.config["UPLOAD_FOLDER"] = "static/"

client = pymongo.MongoClient('localhost',27017)
db = client.user_login_system

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect('/')
    return wrap

from user import routes

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/dashboard/')
@login_required
def dashboard():
    return render_template('dashboard.html')