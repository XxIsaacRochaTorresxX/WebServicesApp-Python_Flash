from flask import render_template
from src.db.mongodb import PyMongo

from src import create_app

varmongo= {"host": "localhost",
           "db": "vinos_jiquilpan",
           "port": 27017,
           "timeout": 1000,
           "user": "",
           "password": ""
           }


app = create_app()

# Ruta principal

@app.route('/')
def index():
    # Abrir BAse de Datos
    objPyMongo = PyMongo(varmongo)
    # Consultar
    objPyMongo.conectar_mongodb()
    campos = {"_id": 0,
              "idCategoria": 1,
              "nombreCategoria": 1,
              "imagenCategoria": 1}
    lista_categorias = objPyMongo.consulta_mongodb('categorias', {}, campos)
    campos = {
        "_id": 0,
        "idProducto": 1,
        "productoNombreCorto": 1,
        "productoTipo": 1,
        "productoImagen": 1,
        "idCategoria.nombreCategoriaProducto": 1
    }
    lista_productos = objPyMongo.consulta_general_productos('productos')
    # Cerrar la conexion
    objPyMongo.desconectar_mongodb()
    # Imprimir categorias
    print(lista_categorias)
    print(lista_productos)
    # Regresamos categorias
    return render_template('index.html',
                           categorias=lista_categorias["resultado"],
                           productos=lista_productos["resultado"])  # 'OK'


if __name__ == '__main__':
    app.run() #debug=True, port=5000