import re
from flask import render_template, request, redirect
from app import db
from app import models
from app.models import Usuario
import json

def index():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if not email or not password:
            return "Falta agregar el email o la contraseña"
        try:
            login = Usuario.query.filter(Usuario.email == email).first()
            if login == None or login.email != email:
                return "Invalid email or password"
            else:
                return redirect("/choose")
        except Exception as err:
            print(err)
            return "Error al concentarse con la base de datos"
    return render_template("index.html")

def register():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        adress = request.form['adress']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        try:
            newUser = models.Usuario(username=username, email=email, password=password,name=name,phone=phone,adress=adress)
            db.session.add(newUser)
            db.session.commit()
        except Exception as err:
            return "username already exists or email already exists"
        return redirect("/choose")

    return render_template("register.html")
    
def choose():
    return render_template("choose.html")