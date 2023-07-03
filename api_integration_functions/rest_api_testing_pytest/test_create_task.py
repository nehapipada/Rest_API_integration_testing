from api_integration_functions.rest_api_function_defination.config import *
from api_integration_functions.rest_api_function_defination.create_task import *
from api_integration_functions.rest_api_function_defination.get_task import *
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