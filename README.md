# Flask Tasks App - **CRUD** 

> [!NOTE]
> Esta aplicación utiliza la versión de Pyhton 3.11.9.

## Pasos para clonar la aplicación:

1. Crear una nueva carpeta en donde copiaras el repositorio.
2. Con Git instalado abrir un bash de git.
3. En el bash de git escribir `git clone https://github.com/AngelPy/Flask_tasks_app.git`.
4. El repositorio con todos las carpetas y archivos esenciales será copiado en la carpeta donde hayas ejecutado el código.

## Pasos para correr la aplicación:

1. Abrir la carpeta con VSCode.
2. Abrir una terminal presionando F1 y buscando toggle terminal.
3. Cambiar el tipo de terminal a cmd en caso de ser necesario.
4. Con el cmd abierto dentro de la terminal crear un entorno virtual con python escribiendo el comando `python -m venv .venv`
5. Luego de haber creado el entorno virtual activarlo para instalar todo lo que necesita la API para ejecutarse.
6. Para ejecutar el entorno virtual escribir el comando `.venv\scripts\activate`
7. Tras haberse cersiorado de la activación del entorno virtual instalar todos los paquetes encontrados en **requirements.txt**.
8. El comando para instalar los paquetes es `pip install -r requirements.txt`
9. Tras haber instalado todos los paquetes ya podrás correr la aplicación en el servidor.
10. Antes de eso deberás realizar las migraciones a la base de datos para poder trabajarla.

## Migraciones:

Con la terminal abierta y el entorno virtual activado escribir los siguientes comandos:
```
flask db init
flask db migrate
flask db upgrade
```
> [!NOTE]
> Esto asegurara que tanto la base de datos como la tabla sean creadas para conseguir realizar cambios en las mismas y poder trabajar con ellas.

## Ejecutar la aplicación:

### Hay 2 opciones:
 - Escribir el comando flask run --debug para ejecutar la aplicación con el debugger activo
 - Escribir el Comando flask run para ejecutar la aplicación sin el debugger

