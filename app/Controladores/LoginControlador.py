from app.__int__ import app
import re
from flask import render_template, request, redirect
from app.__int__ import db
from app.models import User
import requests
import json

def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if not username or not password:
            return "El usuario o la contraseña son incorrectos"
        try:
            user = User.query.filter(User.username=username).first()
            if user == None or pasword != user.pasword:
                return "Usuario o Contraseña Invalidos"
            email = user.email
        except Exception as err:
            print(err)
            return "Ocurrio un error al entrar a tu usuario. Intealo de nuevo"
    return reder_templaye("login.html")