import requests
from api_integration_functions.rest_api_function_defination.config import *
def  list_tasks(user_id):
    return requests.get(ENDPOINT + f"list-tasks/{user_id}")