from flask import Blueprint
from flask import render_template, request, redirect, url_for, flash, jsonify
from werkzeug.security import generate_password_hash
from flask_login import login_user, logout_user
from werkzeug.security import check_password_hash
from utils.db import db

# Importacion de Modelos
from models.entities.usuario import usuario, UserSchema
from models.entities.User import User

sesiones = Blueprint('sesiones', __name__)

# RenderInicioSesion
@sesiones.route('/IniSes', methods=['GET','POST'])
def InicioSesion():

    if request.method == 'POST':
        # print(request.form['email'])
        # print(request.form['password'])
        contra = request.form['password']
        try:
            result=None
            result = db.session.query(usuario).filter(usuario.correo == request.form['email'])
            
            for i in result:
                us = User(i.id,i.nombre,i.apellido,i.correo,contra,i.administrador)
                if not us or not check_password_hash(i.contraseña, contra):
                    flash('Please check your login details and try again.')
                    return render_template('html/InicioSesion.html')
                else:
                    logged_user = us
                    login_user(logged_user)
                    return redirect(url_for('estatico.index'))
        except Exception as ex:
            return render_template('html/InicoSesion/InicioSesion.html')
    else:
        return render_template('html/InicoSesion/InicioSesion.html')


#Registrar Usuarios API
@sesiones.route('/RegistroUsuario', methods=['POST'])
def RegistroUsuario():

    create_user = {}

    create_user["nombre"] = request.form['nombre']
    create_user["apellido"] = request.form['apellido']
    create_user["correo"] = request.form['email']
    create_user["contraseña"] = generate_password_hash(request.form['password'])
    create_user["administrador"] = 0
    
    schema = UserSchema()
    usu = schema.load(create_user)

    print(usu)

    db.session.add(usu)
    db.session.commit()

    return redirect(url_for('sesiones.InicioSesion'))

# RenderRegistro
@sesiones.route('/Registro', methods=['GET'])
def Registro():
    return render_template('html/InicoSesion/Registrarse.html')

    

@sesiones.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('sesiones.InicioSesion'))