import re
from flask import render_template, request, redirect
from app import db
from app import models
from app.models import Usuario

def Vender():
    return render_template("Vender.html")