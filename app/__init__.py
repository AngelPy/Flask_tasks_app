from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
import os

# Variables para inicializar las instancias de SQLAlchemy y Marshmallow que nos permitiran utilizarlas
# en el resto del código, como en los modelos, esquemas y tareas.
db = SQLAlchemy()
ma = Marshmallow()

# Creo una función para correr la aplicación, donde está el código necesario para correr la aplicación
# y evitar importaciones circulares que presenten errores al momento de correr el servidor.
def create_app():

    # Primero se declara una variable app que llevara como valor a la aplicación de Flask.
    app = Flask(__name__)

    # Configuramos la Uri de SQLALCHEMY trayendola desde el archivo de variables de entorno
    # haciendo uso de os.
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')

    # Se inicializan las variables tanto de SQLAlchemy y Marshmallow para ser utilizadas en
    # el resto del código.
    db.init_app(app)
    ma.init_app(app)
    
    # Realizo una importación de la variable api que es el Blueprint de mis rutas, la cual se ubica en routes.py.
    from app.routes import api

    # Registro la Blueprint y le asigno un prefijo para cada una de las rutas que la utilicen, el prefijo será: /api.
    app.register_blueprint(api, url_prefix='/api')

    # Realizo la migración pasandole a la variable migrate los parametros app y db.
    migrate = Migrate(app, db)

    # Por ultimo retorno la variable app para poder correr la aplicación desde la función
    return app
