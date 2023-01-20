from flask import Blueprint, request, jsonify
from ..extensiones import db
from ..models import Clientes

#Definir blue print para cliente
cliente = Blueprint('cliente',__name__)
#Definir la ruta CLIENTES
@cliente.route('/api/clientes',methods=['GET','POST'])
def consultar_cliente():
    clientes=db.session.query(Clientes).all()
    print(clientes)
    return {'mensaje':'Consultando Clientes'}
#Definir la ruta CLIENTES
@cliente.route('/api/clientes/registrar',methods=['POST'])
def insertar_cliente():
    # Leer los datos enviados
    # REcibir desde un formulario request.form['nombre']

    json_cliente = request.get_json()
    #for clave, valor in json_cliente.items():
     #   print(clave, valor)

    cliente = Clientes()
    return  jsonify( cliente.registrar_cliente(json_cliente))
    
    # for clave,valor in json_cliente.items():
    #     print(clave,valor)
    
    # return {'mensaje':'Insertando Cliente'}


@cliente.route('/api/clientes/login',methods=['POST'])
def login_cliente():
    json_cliente = request.get_json()

    for clave,valor in json_cliente.items():
        print(clave,valor)

    cliente = Clientes()
    return jsonify(cliente.validar_cliente(json_cliente['correo'], json_cliente['clave']))
