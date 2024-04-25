from flask import request, jsonify
from app.models import Tasks, task_schema, tasks_schema
from app import db, ma
from marshmallow.exceptions import ValidationError

def show_tasks():
    tasks = Tasks.query.all()
    return tasks_schema.dump(tasks)

def create_task():
    data = request.get_json()
    
    try:
        task = task_schema.load(data)
    except ValidationError as err:
        return jsonify({"msg": "Validation Error"}), 400

    db.session.add(task)
    db.session.commit()

    return task_schema.dump(task), 201
    
def delete_task(id):
    data = request.get_json()

    task = db.get_or_404(Tasks, id)
    db.session.delete(task)
    db.session.commit()

    return show_tasks(), 201

def edit_task(id):
    data = request.get_json()
    old_task = Tasks.query.get(id)

    try:
        task = task_schema.load(data)
    except ValidationError as err:
        return jsonify({"msg": "Validation Error"}), 400
    
    old_task.title = task.title
    old_task.description = task.description

    db.session.commit()


    return jsonify({
        "status": 200,
        "msg": "Updated Succesfully"
    })