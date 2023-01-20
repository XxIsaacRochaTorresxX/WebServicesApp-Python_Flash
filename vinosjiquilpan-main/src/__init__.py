
from flask import Flask
from flask_cors import CORS

# from src.categorias.routes import categoria

def create_app():
    app = Flask(__name__)
    # Configurar las referencias cruzadas, cuando se hacen peticiones de otros dominios
    CORS(app)
    # Agregar configuración desde archivo configuracion.txt
    #app.config.from_object('configuracion.DevConfig')
    app.config.from_pyfile('configuracion.py')


    # Registramos los Blueprints
    from .categorias import categoria
    app.register_blueprint(categoria)

    from .productos import producto
    app.register_blueprint(producto)

    from .clientes import cliente
    app.register_blueprint(cliente)

    from .pedidos import pedido
    app.register_blueprint(pedido)


    return app