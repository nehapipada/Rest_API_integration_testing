import requests
ENDPOINT ="https://todo.pixegami.io/"

response = requests.get(ENDPOINT)
print(response)
data = response.json()
print(data)
status_code=response.status_code
print(status_code)

def test_can_call_endpoint():
    response= requests.get(ENDPOINT)
    assert response.status_code == 200
def test_can_create_task():
    payload =  new_task_payload()
    create_task_response =create_task(payload)
    assert create_task_response.status_code == 200
    data=create_task_response.json()
    print(data)
    task_id = data["task"]["task_id"]
    get_task_response = get_task(task_id)
    assert get_task_response.status_code==200
    get_task_data=get_task_response.json()
    assert get_task_data["content"]==payload["content"]
   # assert get_task_data["task_id"]==payload["task_id"]
    assert get_task_data["user_id"]==payload["user_id"]
    #get_task_data=get_task_response.json()
    print(get_task_data)

def test_can_update_task():
     payload=new_task_payload()
     create_task_response=create_task(payload)
     task_id = create_task_response.json()["task"]["task_id"]
     new_payload = {
         "user_id": payload["user_id"],
         "task_id": task_id,
         "content":"my updated content",
         "is_done":True
     }
     update_task_response = update_task(new_payload)
     assert update_task_response.status_code==200

def test_can_list_users():
    N=3
    for _ in range(N):
        payload = new_task_payload()
        create_task_response = create_task(payload)
        assert create_task_response.status_code==200
    list_task_response=list_tasks("test_user")
    assert list_task_response.status_code==200

def test_can_delete_task():
    payload=new_task_payload()
    create_task_response=create_task(payload)
    assert create_task_response.status_code==200
    task_id = create_task_response.json()["task"]["task_id"]

    delete_task_response=delete_tasks(task_id)
    assert delete_task_response.status_code==200
def create_task(payload):
    return requests.put(ENDPOINT + "/create-task",json=payload)

def update_task(payload):
    return requests.put(ENDPOINT+ "/update-task",json=payload)
def get_task(task_id):
    return  requests.get(ENDPOINT + f"/get-task/{task_id}")
def  list_tasks(user_id):
    return requests.get(ENDPOINT + f"list-tasks/{user_id}")
def delete_tasks(task_id):
    return requests.delete(ENDPOINT + f"/delete-task/{task_id}")
def new_task_payload():
    return {
        "content":"my test content",
        "user_id": "test_user",
        "is_done": False
    }
