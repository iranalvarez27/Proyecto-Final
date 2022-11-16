import re
from flask import render_template, request, redirect
from app import db
from app import models
from app.models import Usuario,Product


import json

def index():
    print(request)
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
        id = request.form['id']
        name = request.form['Name']
        phone = request.form['Phone']
        adress = request.form['adress']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        try:
            newUser = models.Usuario(id=id,name=name,phone=phone,adress=adress,username=username,email=email,password=password)
            db.session.add(newUser)
            db.session.commit()
        except Exception as err:
            print (err)
            return "username already exists or email already exists"
        return redirect("/choose")

    return render_template("register.html")
    
def choose():
    return render_template("choose.html")
def vender():
    return render_template("Vender.html")
def productos():
    return render_template("Productos.html")

def registrar_producto():
    if request.method == 'POST':
        p_id = request.form['Codigo']
        p_name = request.form['Nombre']
        p_price = request.form['Precio']
        p_stock = request.form['stock']
        p_description = request.form['Descripción']
        p_brand = request.form['Marca']
        p_category = request.form['Categoria']



        try:
            newProduct = models.Product(p_id=p_id,p_name=p_name,p_price=p_price,p_stock=p_stock,p_description=p_description,p_brand=p_brand,p_category=p_category
            db.session.add(newProduct)
            db.session.commit()
        except Exception as err:
            print (err)
            return "Tu producto no se pudo registrar intenta de nuevo"
        return redirect("/productos")
    return render_template("registrar_producto.html")