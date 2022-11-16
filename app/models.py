from app import db
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship,backref

class Usuario(db.Model):
    __tablename__ ="Usuarios"
    #info basica para las ventas
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True) #id para pedidos
    name = db.Column(db.String(80),index=True ,nullable=False) #nombre real
    phone = db.Column(db.String(9),index=True , nullable=False) #9 digitos
    adress = db.Column(db.String(120),index=True  ,nullable=False) #direccion tienda fisica
    #info para el register
    username = db.Column(db.String(80), unique=True, nullable=False) #nombre usuario
    email = db.Column(db.String(120), unique=True, nullable=False) #correo personal
    password = db.Column(db.String(120), nullable=False) # Encriptar
    
    def __repr__(self):
        return '<Usuario {}>'.format(self.username)

class Product(db.Model):
    __tablename__ ="Productos"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    p_id = db.Column(db.String(6), unique=True, nullable=False) 
    p_name = db.Column(db.String(80), nullable=False) #nombre real
    p_price = db.Column(db.Float, nullable=False) #precio
    p_stock = db.Column(db.Integer, nullable=False) #stock
    p_description = db.Column(db.String(120), nullable=False) #descripcion del producto
    p_brand = db.Column(db.String(120), nullable=False) #marca del producto
    p_category = db.Column(db.String(120), nullable=False) #categoria del producto 
    usuario_nom = db.Column(db.String(80), db.ForeignKey('Usuarios.username')) 
    Usuario = relationship("Usuario",backref=backref("Productos",cascade="all, delete-orphan"))
    
    def __repr__(self):
        return '<Product {}>'.format(self.p_name)

class Compra(db.Model):
    __tablename__ ="Compra"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    c_registro = db.Column(db.DateTime, nullable=False) #fecha de registro
    c_descripcion =   db.Column(db.String(120), nullable=False) #descripcion de la compra
    user_idc = db.Column(db.Integer,db.ForeignKey("Usuarios.id"))
    product_idc = db.Column(db.Integer,db.ForeignKey("Productos.id"))
    Product = relationship(Product,backref=backref("Compra",cascade="all, delete-orphan"))
    Usuario = relationship(Usuario,backref=backref("Compra",cascade="all, delete-orphan"))

    def _repr_(self):
        return '<Compra {}>'.format(self.c_registro)