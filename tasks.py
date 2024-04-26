# Se importa la funcion create_app para correr la aplicación en este archivo.
from app import create_app

# Declaro una variable flask_run para poder correr el servidor, esta tiene como valor la función
# create_app() y a través de este valor podremos correr el servidor llamando al metodo .run().
flask_run = create_app()

if __name__ == '__main__':
    
    # ejecutamos el metodo .run() propio de la variable flask_run para inicializar el servidor.i
    flask_run.run()