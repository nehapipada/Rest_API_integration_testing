from api_integration_functions.rest_api_function_defination.config import *
from api_integration_functions.rest_api_function_defination.create_task import *
from api_integration_functions.rest_api_function_defination.update_task import *
def test_can_update_task():
    payload = new_task_payload()
    create_task_response = create_task(payload)
    task_id = create_task_response.json()["task"]["task_id"]
    new_payload = {
        "user_id": payload["user_id"],
        "task_id": task_id,
        "content": "my updated content",
        "is_done": True
    }
    update_task_response = update_task(new_payload)
    assert update_task_response.status_code == 200
