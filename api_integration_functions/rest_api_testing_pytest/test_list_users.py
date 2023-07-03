from api_integration_functions.rest_api_function_defination.config import *
from api_integration_functions.rest_api_function_defination.create_task import *
from api_integration_functions.rest_api_function_defination.list_tasks import *
def test_can_list_users():
    N=3
    for _ in range(N):
        payload = new_task_payload()
        create_task_response = create_task(payload)
        assert create_task_response.status_code==200
    list_task_response=list_tasks("test_user")
    assert list_task_response.status_code==200