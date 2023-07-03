import requests
from api_integration_functions.rest_api_function_defination.config import *
def update_task(payload):
    return requests.put(ENDPOINT+ "/update-task",json=payload)