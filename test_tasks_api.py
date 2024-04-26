import requests

ENDPOINT = "http://localhost:5000/api"

def test_can_call_endpoint():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200

def test_can_create_task_and_show_task_by_id():
    payload = new_task_payload()
    
    create_task_response = create_task(payload)
    assert create_task_response.status_code == 200

    task_id = create_task_response.json()["id"]
    
    get_task_byid_response =  get_task_by_id(task_id)
    assert get_task_byid_response.status_code == 200

def test_can_delete_task_by_id():
    payload = new_task_payload()

    create_task_response = create_task(payload)
    task_id = create_task_response.json()["id"]

    delete_task_response = delete_task(task_id)
    assert delete_task_response.status_code == 200

    get_task_byid_response = get_task_by_id(task_id)
    assert get_task_byid_response.status_code == 200

def test_can_edit_task_by_id():
    payload = new_task_payload()
    new_payload = new_task_edited_payload()

    create_task_response = create_task(payload)
    task_id = create_task_response.json()["id"]

    edit_task_response = requests.put(ENDPOINT + f"/update/{task_id}", json=new_payload)
    assert edit_task_response.status_code == 200

    get_edited_task = get_task_by_id(task_id)
    assert get_edited_task.status_code == 200


def create_task(payload):
    return requests.post(ENDPOINT + "/insert", json=payload)

def delete_task(task_id):
    return requests.delete(ENDPOINT + f"/delete/{task_id}")


def new_task_payload():
    return {
        "title": "Test Title",
        "description": "Test Description"
    }

def new_task_edited_payload():
    return {
        "title": "Test Edited Title",
        "description": "Test Edited Description"
    }

def get_task_by_id(task_id):
    return requests.get(ENDPOINT + f"/{task_id}")