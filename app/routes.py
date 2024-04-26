# Rutas donde se realizarán los metodos http

from flask import Blueprint, request
from app.models import Tasks
from app.controller.tasks import show_tasks, create_task, delete_task, edit_task, get_task_by_id

# Definimos la variable Blueprint que nos permitirá manejar las rutas de manera ordenada.
api = Blueprint('api', __name__)

# Ruta para mostrar todas las tareas almacenadas en la tabla.
# Llama a la función show_tasks() que contiene el código para mostrar todas las tareas de la tabla.
@api.route('/', methods=['GET'])
def get_tasks():
    return show_tasks()

@api.route('/<int:id>', methods=['GET'])
def get_task_byid(id):
    return get_task_by_id(id)

# Ruta para crear nuevas tareas en la tabla.
# Llama a la funcion create_task() que contiene el código para insertar nuevas tareas a la tabla.
@api.route('/insert', methods=['POST'])
def insert_task():
    return create_task()

# Ruta para eliminar una tarea especifica de la tabla.
# Llama a la funcion delete_task(id) que contiene el código para eliminar tareas por el id ingresado
# en la url.
@api.route('/delete/<int:id>', methods=['DELETE'])
def drop_task(id):
    return delete_task(id)

# Ruta para eliminar una tarea especifica de la tabla.
# Llama a la funcion update_task(id) que contiene el código para editar tareas por el id ingresado
# en la url.
@api.route('/update/<int:id>', methods=['PUT'])
def update_task(id):
    return edit_task(id)