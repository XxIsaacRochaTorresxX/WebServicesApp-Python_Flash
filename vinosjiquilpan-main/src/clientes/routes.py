from flask import render_template, request, flash, redirect, session
import requests


from . import cliente

HOST = 'http://127.0.0.1/:5000' #IPE, puerto

# Crear los endpoints
# Ruta: http://127.0.0.1:5000/clientes
@cliente.route('/registrar', methods=['GET', 'POST'])
def registrar_cliente(): 
    RUTA = '/api/clientes/registrar' #Es la del servidor
    URL = HOST+RUTA
    # Saber cuál método
    #print(request.form.to_dict())saca todo
    if request.method == 'POST':
        #Verificar que los datos no estén repetidos
        if verificar_datos(request.form.to_dict()):
            #Llamado a la api
            respuesta=requests.post(URL, json=request.form.to_dict()) #Petición al servidor
            #print(respuesta.json())
            flash(respuesta.json()['mensaje'])
        else:
            flash('No se permiten valores nulos...')
    return render_template('/clientes/registro.html')

@cliente.route('/login', methods=['GET', 'POST'])
def login_cliente(): 
    RUTA = '/api/clientes/login' #Es la del servidor
    URL = HOST+RUTA
    # Saber cuál método
    #print(request.form.to_dict())saca todo
    if request.method == 'POST':
        #Verificar que los datos no estén repetidos
        if verificar_datos(request.form.to_dict()):
            #Llamado a la api
            respuesta=requests.post(URL, json=request.form.to_dict()) #Petición al servidor
            #print(respuesta.json())
            if respuesta.json()['status'] == 'OK-1':
                #CREAR VARIABLES DE SESIÓN
                session['token'] = respuesta.json()['token']
                session['nombre'] = respuesta.json()['datos']['nombre']
                return redirect('/')
            flash(respuesta.json()['mensaje'])
        #else:
        #    flash('No se permiten valores nulos...')
    return render_template('/clientes/login.html')




def verificar_datos(datos):
    for indice, valor in datos.items():
        if valor =='' or valor == None:
            return False
    return True