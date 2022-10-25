from app import db
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship,backref

class Usuario(db.Model):
    __tablename__ ="Usuario"
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
    usuario = relationship("Product",secondary="compra")
    usuario = relationship("Product",secondary="venta")
    def __repr__(self):
        return '<User {}>'.format(self.username)

class Product(db.Model):
    __tablename__ ="Product"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    p_id = db.Column(db.String(6), unique=True, nullable=False) 
    p_name = db.Column(db.String(80), nullable=False) #nombre real
    p_price = db.Column(db.Float, nullable=False) #precio
    p_stock = db.Column(db.Integer, nullable=False) #stock
    p_description = db.Column(db.String(120), nullable=False) #descripcion del producto
    p_brand = db.Column(db.String(120), nullable=False) #marca del producto
    p_due_date = db.Column(db.String(120), nullable=False) #fecha de caducidad
    productos = relationship("Usuario",secondary="compra")
    productos = relationship("Usuario",secondary="venta")
    
    def __repr__(self):
        return '<Product {}>'.format(self.p_name)
class Compra(db.Model):
    __tablename__ ="Compra"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    c_registro = db.Column(db.DateTime, nullable=False) #fecha de registro
    c_descripcion =   db.Column(db.String(120), nullable=False) #descripcion de la compra
    user_id = db.Column(db.Integer,db.ForeignKey("Usuario.id"))
    product_id = db.Column(db.Integer,db.ForeignKey("Product.id"))
    producto = relationship(Product,backref=backref("Compra",cascade="all, delete-orphan"))
    usuario = relationship(Usuario,backref=backref("Compra",cascade="all, delete-orphan"))

    def _repr_(self):
        return '<Ventas {}>'.format(self.c_registro)

class Venta(db.Model):
    __tablename__ ="Venta"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    v_descripcion =   db.Column(db.String(120), nullable=False) #descripcion de la venta
    p_codigo = db.Column(db.String(6), db.ForeignKey('Producto.p_id'), nullable=False) #codigo del producto
    u_dni = db.Column(db.String(8), db.ForeignKey('Usuario.id'), nullable=False) #dni del usuario
    user_id = db.Column(db.Integer,db.ForeignKey("Usuario.id"))
    product_id = db.Column(db.Integer,db.ForeignKey("Product.id"))
    producto = relationship(Product,backref=backref("Venta",cascade="all, delete-orphan"))
    usuario = relationship(Usuario,backref=backref("Venta",cascade="all, delete-orphan"))

    def _repr_(self):
        return '<Ventas {}>'.format(self.p_codigo)