from app import db
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

class Usuario(db.Model):
    #info basica para las ventas
    id = db.Column(db.Integer, primary_key=True, autoincrement=True) #id 
   # dni = db.Column(db.String(9), unique=True, nullable=False) #dni para pedidos
    name = db.Column(db.String(80),index=True ,nullable=False) #nombre real
    phone = db.Column(db.String(9),index=True , nullable=False) #9 digitos
    adress = db.Column(db.String(120),index=True  ,nullable=False) #direccion tienda fisica
    #info para el register
    username = db.Column(db.String(80), unique=True, nullable=False) #nombre usuario
    email = db.Column(db.String(120), unique=True, nullable=False) #correo personal
    password = db.Column(db.String(120), nullable=False) # Encriptar
    def __repr__(self):
        return '<User {}>'.format(self.username)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    p_id = db.Column(db.String(6), unique=True, nullable=False) 
    p_name = db.Column(db.String(80), nullable=False) #nombre real
    p_price = db.Column(db.Float, nullable=False) #precio
    p_stock = db.Column(db.Integer, nullable=False) #stock
    p_description = db.Column(db.String(120), nullable=False) #descripcion del producto
    p_brand = db.Column(db.String(120), nullable=False) #marca del producto
    p_due_date = db.Column(db.String(120), nullable=False) #fecha de caducidad
    def __repr__(self):
        return '<Product %r>' % self.p_name

class Ventas(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True) #id
    client_adress_ = db.Column(db.String(120), nullable=False) 
    client_name = db.Column(db.String(80), nullable=False) #nombre del cliente
    client_phone = db.Column(db.String(9), nullable=False) #telefono del cliente
    client_dni = db.Column(db.String(9), nullable=False) #dni del cliente
    register_date = db.Column(db.String(120), nullable=False) #fecha de registro
    expected_date = db.Column(db.String(120), nullable=False) #fecha de entrega
    products_description = db.Column(db.String(120), nullable=False) #productos

    def __repr__(self):
        return '<Ventas %r>' % self.client_name