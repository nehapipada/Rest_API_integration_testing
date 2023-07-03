import requests
from api_integration_functions.rest_api_function_defination.config import *
def delete_tasks(task_id):
    return requests.delete(ENDPOINT + f"/delete-task/{task_id}")