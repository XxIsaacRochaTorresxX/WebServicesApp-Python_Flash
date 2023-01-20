from flask import render_template, request

from . import pedido

varmongo= {"host": "localhost",
           "db": "vinos_jiquilpan",
           "port": 27017,
           "timeout": 1000,
           "user": "",
           "password": ""
           }

# Crear los endpoints
# Ruta: http://127.0.0.1:5000/productos
@pedido.route('/carrito')
def ver_carrito(): 

   
    return render_template('/pedidos/carrito.html')

@pedido.route('/checkout')
def verificar_cuenta():
    return 'desde cuenta...'


