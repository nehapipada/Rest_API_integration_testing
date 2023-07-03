import requests
from api_integration_functions.rest_api_function_defination.config import *
def get_task(task_id):
    return  requests.get(ENDPOINT + f"/get-task/{task_id}")