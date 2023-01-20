from .extensiones import db
from sqlalchemy import Column, ForeignKey,Integer,String,Boolean,exc
import datetime
import bcrypt
import jwt


class Clientes(db.Model):
    __name__='clientes'
    id=db.Column(db.Integer,primary_key=True)
    clienteNombre= db.Column(db.String(100), nullable=False)
    clienteApellidos= db.Column(db.String(100), nullable=False)
    clienteRFC= db.Column(db.String(100))
    clienteEmail= db.Column(db.String(100), nullable=False, unique=True)
    clientePassword = db.Column(db.String(200), nullable=False)
    confirmado =  db.Column(db.Boolean,default=False)
    # pedidos = db.relationship('Pedidos', backref='clientes')
    def registrar_cliente(self,datos):
        msg="Cliente insertado correctamente"
        respuesta={'status': 'OK', 'codigo':'','mensaje':msg}
        self.clienteNombre =  datos['nombre']
        self.clienteEmail = datos['correo']
        self.clientePassword = self.cifrar_contrasena(datos['clave'])
        

        try:
            db.session.add(self)
            db.session.commit()
            respuesta["codigo"] = '1'

            
        except exc.SQLAlchemyError as error:
            print(error)
            valor = (error.__cause__.args[1].split("'"[1]))
            campo = (error.__cause__.args[1].split("'"[3]))

            msj_error='Ocurrió un error para el campo: ' + campo + " en la entrada de datos: " + valor
        
            respuesta["codigo"] = error.__cause__.args[0]
            respuesta["mensaje"] = msj_error
        return respuesta
    
    def cifrar_contrasena(self, contrasena):
        salt = bcrypt.gensalt()
        contrasena_cifrada = bcrypt.hashpw(contrasena.encode('utf-8'),salt)
        return contrasena_cifrada

    def verificar_contrasena(self, clave, clave_cifrada):
        return bcrypt.checkpw(clave.encode('utf-8'), clave_cifrada.encode('utf-8'))
    
    def validar_cliente(self, correo,clave):
        #1. Respuestaa
        msg="Cliente Aurorizado"
        respuesta={
                   'status': 'OK-1', 
                   'codigo':'1',
                   'mensaje':msg, 
                   "token":"", 
                   "datos":{}
                   }

        #2.Crear Consulta
        cli = Clientes.query.filter(Clientes.clienteEmail == correo).first()

        if cli:
            #Vericificar la contraseña
            if self.verificar_contrasena(clave, cli.clientePassword):
                msg = "Cliente Autenticado"
                respuesta["mensaje"] = msg
                #Generar Token
                respuesta["token"] = self.generar_token(cli)
                respuesta["datos"] = {
            'id': cli.id,
            'nombre': cli.clienteNombre,
            'apellidos': cli.clienteApellidos,
            'correo': cli.clienteEmail
            }
                respuesta['status']= "OK-1"
            else:
                msg = "Cliente No autenticado"
                respuesta["mensaje"]= msg
                respuesta['codigo']= "0"
                respuesta['status']= "OK-0"
        else:
            msg="Cliente no existe"
            respuesta['status']="OK-0"
        respuesta["mensaje"]=msg
        return respuesta
    
    def generar_token(self, cliente):
        secreto = "Palabra_Secreta" #traidadesde configuracion
        token = jwt.encode({
            'id': cliente.id,
            'nombre': cliente.clienteNombre,
            'apellidos': cliente.clienteApellidos,
            'correo': cliente.clienteEmail

        },
      
        secreto,
        algorithm = 'HS256'
        )
        return token
    
class Categoria(db.Model):
    __tablename__='categorias'
    id=db.Column(db.Integer,primary_key=True)
    nombreCategoria=db.Column(db.String(100),nullable=True)
    descripcionCategoria=db.Column(db.String(400))
    banderaDescuento=db.Column(db.Integer,default=0)
    descuentoCategoria=db.Column(db.Integer,default=0)
    imagenCategoria=db.Column(db.String(50),default='imagenDefault.jpg')
    productos = db.relationship('Productos', backref='categorias')
class Productos(db.Model):
    __tablename__='productos'
    id=Column(Integer,primary_key=True)
    idCategoria=Column(Integer,ForeignKey('categorias.id'))
    productoNombreCorto = Column(String(100),unique=True)
    productoNombreLargo = Column(String(200))
    productoDescripcion = Column(String(200))
    productoTipo = Column(Integer,default=1)
    productoPresentacion = Column(String(20),default='botella')
    productoCosto = Column(Integer,nullable=False)
    productoGanancia = Column(Integer,nullable=False,default=20)
    productoDescuento = Column(Integer,default=0)
    productoExistencia = Column(Integer,default=1000)
    productoImagen = Column(String(50),default='imagenDefault.jpg')

detalle_pedidos=db.Table('detallepedidos',
    db.Column('id',db.Integer,primary_key=True),
    db.Column('idProducto',db.Integer,db.ForeignKey('productos.id')),
    db.Column('idPedido',db.Integer,db.ForeignKey('pedidos.id')),
    db.Column('cantidad',db.Integer,nullable=False),
    db.Column('descuento',db.Integer,default=0),
    db.Column('precioFinal',db.Integer,nullable=False),
    db.Column('subTotal',db.Integer,nullable=False)
)

class Pedidos(db.Model):
    __name__='pedidos'
    id = Column(Integer,primary_key=True)
    idCliente = Column(Integer , ForeignKey('clientes.id'))
    total=Column(Integer,default=0.0)
    iva=Column(Integer,nullable=False)
    descuento = Column(Integer,default=0.0  )
    pagado = Column(Boolean, default = False)
    estado = Column(Integer, default=1)

    # Establecer la relacion de muchos a muchos con detallepedidos
    producto_pedidos= db.relationship('Productos',
                                      secondary= detalle_pedidos,
                                      backref=db.backref('pedidos'))


