
from flask import Flask
from flask_cors import CORS
from .configuracion import DevConfig

from .extensiones import db
from .routes.clientesRoutes import cliente
from .routes.categoriaRoutes import categoria
from .routes.productoRoutes import productos

# from src.categorias.routes import categoria

def create_app():
    app = Flask(__name__)
    # Configurar las referencias cruzadas, cuando se hacen peticiones de otros dominios
    CORS(app)
    # Agregar configuración desde archivo configuracion.txt
    app.config.from_object(DevConfig)
    #app.config.from_pyfile('configuracion.py')
    # Configurar SQLAlchemy
    db.init_app(app) #  ***************FALTÓ PASARLE LA APLICACIÓN (app)

    # Registramos los Blueprints
    app.register_blueprint(cliente)
    app.register_blueprint(categoria)
    app.register_blueprint(productos)

    return app

