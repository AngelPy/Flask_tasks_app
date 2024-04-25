from flask import Blueprint, request
from app.models import Tasks
from app.controller.tasks import show_tasks, create_task, delete_task, edit_task

api = Blueprint('api', __name__)

@api.route('/', methods=['GET'])
def get_tasks():
    if request.method == 'GET':
        return show_tasks()
    else:
        return jsonify({
            "status": 500,
            "msg": "Error"
        })

@api.route('/insert', methods=['POST'])
def insert_task():
    return create_task()

@api.route('/delete/<int:id>', methods=['DELETE'])
def drop_task(id):
    return delete_task(id)

@api.route('/update/<int:id>', methods=['PUT'])
def update_task(id):
    return edit_task(id)