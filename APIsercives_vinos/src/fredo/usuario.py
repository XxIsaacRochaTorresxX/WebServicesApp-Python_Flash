# from werkzeug.security import check_password_hash,generate_password_hash
from utils.db import db
from utils.ma import ma
from marshmallow import fields, post_load, Schema

class usuario(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable = False)
    apellido = db.Column(db.String(100), nullable = False)
    correo = db.Column(db.String(100), unique = True, nullable = False)
    contraseña = db.Column(db.String(150), nullable = False)
    administrador = db.Column(db.Integer, nullable = False, default = 0)


    def __init__(self, nombre, apellido,correo,contraseña,administrador):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.contraseña = contraseña
        self.administrador = administrador

class UserSchema(Schema):
    nombre = fields.String()
    apellido = fields.String()
    correo = fields.Email()
    contraseña = fields.String()
    administrador = fields.Integer()

    @post_load
    def make_usuario(self, data, **kwargs):
        return usuario(**data)
    



