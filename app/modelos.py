from datetime import datetime
from app import db

class User(db.Moldel):
    id = db.Column(db.Interger,primary_key=True,autoincrement=True)
    usuario = db.Column(db.String(64), index=True,unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.usuario)


class Review(db.Model):
    id = db.Column(db.Interger, primary_key=True)
    rating = db.Column(db.String)
    descripcion = db.Column(db.String(120))
    def __repr__(self):
        return '<Estudiante {} {}>'.format(self.rating, self.descripcion)