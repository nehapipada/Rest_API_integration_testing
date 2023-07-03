from api_integration_functions.rest_api_function_defination.config import *
from api_integration_functions.rest_api_function_defination.create_task import *
from api_integration_functions.rest_api_function_defination.delete_tasks import *
def test_can_delete_task():
    payload=new_task_payload()
    create_task_response=create_task(payload)
    assert create_task_response.status_code==200
    task_id = create_task_response.json()["task"]["task_id"]

    delete_task_response=delete_tasks(task_id)
    assert delete_task_response.status_code==200