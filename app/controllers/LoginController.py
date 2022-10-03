from operator import methodcaller
from app import app
import re
from flask import render_template, request, redirect
from app import db
from app import models
from app.models import User
import requests
import json
from cryptography.hazmat.primitives import hashes

def index():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if not email or not password:
            return "Falta agregar el email o la contraseña"
        try:
            login = User.query.filter(User.email == email).first()
            if login == None or login.email != email:
                return "Invalid email or password"
            else:
                return redirect("/perfil")
        except Exception as err:
            print(err)
            return "Error al concentarse con la base de datos"
    return render_template("index.html")

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