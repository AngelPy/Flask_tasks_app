#  Importamos la variables db y ma para construir el modelo y ele squema de las tareas. 
from app import db, ma

# Se realiza una clase tarea que hereda desde db.Model que nos permitirá definir las columnas
# y los tipos de datos de las mismas en la base de datos.
class Tasks(db.Model):

    # Declaro el nombre de la tabla.
    __tablename__ = 'tasks'

    # Declaro las columnas con su tipo de datos, especificando cual es la llave primaria
    # y cuales columnas no pueden recibir datos vacios.
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)

    # Defino la función que se utilizará al intentar imprimir el objeto de esta clase
    # mostrando solo el titulo y la descripción de la tarea.
    def __repr__(self):
        return f'Task title: {self.title}, description: {self.description}'

# Se crea la clase del esquema que hereda de ma.SQLAlchemyAutoSchema que permite crear el esquema
# de forma automática solo indicando el modelo.
class TaskSchema(ma.SQLAlchemyAutoSchema):

    # Se realiza la clase Meta en donde estarán los parametros del esquema:
    class Meta:

        # Se declara que el modelo será el Objeto Tasks, el esquema hará que todas las
        # acciones que afecten a la tabla sean validadas con el modelo de la clase Tasks.
        model = Tasks

        # Declaro como verdadero a la variable load_instance que permitirá cargar los datos
        # enviados via .json en una variable para validaciones, escritura y edición de datos.
        load_instance = True

        # Defino la session de SQLAlchemy para la deserialización de los datos la cual solo es necesitada
        # cuando load_instance es verdadero.
        sqla_session = db.session

# Por ultimo declaro dos variables de tipo TaskSchema para poder retornar los datos
# entregados al esquema.

# task_schema trabaja con 1 solo objeto.
task_schema = TaskSchema()

# tasks_schema trabaja con mas de 1 objeto puesto que tiene como propiedad 'many' que es verdadero
tasks_schema = TaskSchema(many=True)