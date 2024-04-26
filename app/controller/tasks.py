from flask import request, jsonify
from app.models import Tasks, task_schema, tasks_schema
from app import db
from marshmallow.exceptions import ValidationError

# Función para mostrar todas las tareas creadas en la tabla 'tasks'
def show_tasks():

    # Query para llamar a todas las tareas encontradas en la tabla
    tasks = Tasks.query.all()

    # Validación que permite verificar si no hay tareas creadas en la tabla.

    # Debido a que la variable tasks realiza el query a través de la clase Tasks
    # el valor de retorno es un objeto vacío '[]'
    if tasks == []:
        # Mensaje de retorno
        return jsonify({
            "msg": "There are no tasks. Create one!"
        })

    # En caso de que el objeto retornado no esté vacio se retorna el esquema 
    # de las tareas que estan en la tabla

    # tasks_schema.dump funciona para retornar el esquema completo con las columnas
    # de la tabla como un .json, los valores que se asignan son los obtenidos en el query almacenado
    # en la variable tasks
    return tasks_schema.dump(tasks)

# Busca 1 sola tarea por su id al ser creado. El Id es insertado en la url.
def get_task_by_id(id):

    # Realiza una consulta a la tabla en donde busca a la tarea por su Id, Id que
    # es enviado por la url del request.
    task = Tasks.query.get(id)

    # En caso de no encontrarla se retorna un mensaje indicando que no se logró
    # encontrar la tarea por el id ingresado.
    if task is None:
        return jsonify({
            "msg": "Couldn't find the task"
        })

    # Retorna los valores de la nueva tarea encontrada como un .json
    return task_schema.dump(task), 200



# Función para crear nuevas tareas.
def create_task():

    # Primero se obtienen todos los datos del archivo .json que recibe la función.
    data = request.get_json()
    
    # Se realiza una validación que permite verificar que los datos recibidos
    # coincidan con las "columnas" encontradas en el modelo de tareas, esto para
    # evitar que al insertar aparezca un error por ingresar datos en una columna que no existe.
    try:
        # se carga el esquema de tarea y se le envían los valores del json encontrado (data).
        task = task_schema.load(data)

    except ValidationError:
        # Al encontrar un error en la validación este encuentra la excepción y envía un json con
        # un mensaje de error.
        return jsonify({"msg": "Validation Error"}), 400

    # Si todo sale bien la base de datos realiza un query para insertar datos,
    # los datos que toma son los cargados en la variable task.
    db.session.add(task)
    db.session.commit()

    # Retorna los valores de la nueva tarea insertada como un .json
    return task_schema.dump(task), 200
    
# Funcion para eliminar tareas.
def delete_task(id):

    # Realiza una consulta a la tabla en donde busca a la tarea por su Id, Id que
    # es enviado por la url del request.
    task = Tasks.query.get(id)

    # En caso de no encontrarla se retorna un mensaje indicando que no se logró
    # encontrar la tarea por el id ingresado.
    if task is None:
        return jsonify({
            "msg": "Couldn't find the task"
        })

    # Si la consulta logra encontrar una tarea por el Id indicado se procede a
    # eliminar de la tabla.
    else:
        db.session.delete(task)
        db.session.commit()

        # Por ultimo retorna un mensaje de éxito.
        return jsonify({
            "msg":"Deleted Succesfully"}), 200
    
    # En caso de encontrar algún otro error que no haya permitido ninguna de las acciones
    # retorna un .json con un mensaje de error.
    return jsonify({
        "msg":"error"
    })

# Función para editar las tareas.
def edit_task(id):

    # Primero se obtienen todos los datos del archivo .json que recibe la función.
    data = request.get_json()

    # Declaro una variable llamada 'old_task' para almacenar los datos a reemplazar de la tarea
    # encontrada por la consulta que busca sobre el Id de la url.
    old_task = Tasks.query.get(id)

    # En caso de no encontrarla se retorna un mensaje indicando que no se logró
    # encontrar la tarea por el id ingresado.
    if old_task is None:
        return jsonify({
            "msg": "Couldn't find the task"
        })

    else:
        # De lo contrario, se realiza una validación que permite verificar que los datos recibidos
        # coincidan con las "columnas" encontradas en el modelo de tareas, esto para evitar que 
        #al insertar aparezca un error por ingresar datos en una columna que no existe.
        try:
            task = task_schema.load(data)
        except ValidationError as err:
            return jsonify({"msg": "Validation Error"}), 400

        # Si la validación es exitosa se sobreescriben los datos de la variable 'old_task' por los
        # cargados en la variable task que recibe el esquema cargado con los valores del .json.
        old_task.title = task.title
        old_task.description = task.description

        # Se realiza el cambio en la tabla con commit().
        db.session.commit() 

        # Se retorna un mensaje de éxito que indica que se logró editar o actualizar la tarea de
        # manera exitosa.
        return jsonify({
            "status": 200,
            "msg": "Updated Succesfully"
        })

    # En caso de encontrar algún otro error que no haya permitido ninguna de las acciones
    # retorna un .json con un mensaje de error.  
    return jsonify({
        "msg":"Error"
    })