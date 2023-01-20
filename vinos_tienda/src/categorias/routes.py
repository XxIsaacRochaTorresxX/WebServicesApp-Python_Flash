import json

from flask import render_template
from src.db.mongodb import PyMongo
from . import categoria

varmongo= {"host": "localhost",
           "db": "vinos_jiquilpan",
           "port": 27017,
           "timeout": 1000,
           "user": "",
           "password": ""
           }

# Crear los endpoints
# Ruta: http://127.0.0.1:5000/categorias/get
@categoria.route('/')
def get_categorias():
    # Abrir BAse de Datos
    objPyMongo = PyMongo(varmongo)
    # Consultar
    objPyMongo.conectar_mongodb()
    campos = {"_id": 0, "idCategoria": 1, "nombreCategoria": 1, "imagenCategoria":1 }
    lista_categorias = objPyMongo.consulta_mongodb('categorias',{},campos)
    # Cerrar la conexion
    objPyMongo.desconectar_mongodb()
    # Imprimir categorias
    print(lista_categorias)
    # Regresamos categorias
    return json.dumps(lista_categorias["resultado"]) # render_template('categorias/index.html') # OK'
