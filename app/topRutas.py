from turtle import title
from app import app
from datetime import datetime
import re
from flask import render_template, request
from app.modelos import User, Review
from app import db
import requests
import json
from flask_cors import CORS, cross_origin

@app.route('/')
@app.route('/index')
def index():
    user = {'username':'usuario'}
    return render_template('index.html', title='Home',user=user, elemento1="codigo",elemento2="HTML")
