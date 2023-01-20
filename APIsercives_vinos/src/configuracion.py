

class BaseConfig:
    # Variables de configuración base
    SQLALCHEMY_DATABASE_URI = "mysql://root@localhost/vinos_jiquilpan_opensource"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = True
    DEBUG = True
    SECRET_KEY = "Palabra_Secreta"
    TESTING = True

class DevConfig(BaseConfig):
    # Variables de la clase Padre
    pass

class ProdConfig(BaseConfig):
    DEBUG = False
    TESTING = False