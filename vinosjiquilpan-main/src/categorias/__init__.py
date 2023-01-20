# El archivo __init__ realmente es constructor del módulo categorias
from flask import Blueprint

# Definir el Blueprint
categoria = Blueprint('categoria', __name__, url_prefix='/categorias', template_folder='templates') #

# Le estamos diciendo Blueprint que tiene rutas definidas
from . import routes