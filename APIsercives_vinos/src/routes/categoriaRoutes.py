from flask import Blueprint
from ..extensiones import db
from ..models import Categoria

#Definir blue print para cliente
categoria = Blueprint('categoria',__name__)
#Definir la ruta CLIENTES
@categoria.route('/api/categorias',methods=['GET'])
def consultar_categorias():
    categorias=db.session.query(Categoria).all()
    print(categorias)
    return {'mensaje':'Consultando Categorias'}