from hashlib import new
from app import app
from flask import request, render_template, redirect, url_for
from app import db
from app import models
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        try:
            newUser = models.User(username=username, email=email, password=password)
            db.session.add(newUser)
            db.session.commit()
        except Exception as err:
            return "username already exists or email already exists"
        return redirect("/profile")

    return render_template("register.html")