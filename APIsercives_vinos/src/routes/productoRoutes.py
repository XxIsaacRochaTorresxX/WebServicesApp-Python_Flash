from flask import Blueprint
from ..extensiones import db
from ..models import Productos

#Definir blue print para cliente
productos = Blueprint('productos',__name__)
#Definir la ruta PRODUCTOS
@productos.route('/api/productos',methods=['GET'])
def consultar_productos():
    lista_productos=db.session.query(Productos).all()
    print(lista_productos)
    return {'mensaje':'Consultando Productos'}