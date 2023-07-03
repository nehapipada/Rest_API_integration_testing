import requests
from api_integration_functions.rest_api_function_defination.config import *
def create_task(payload):
    return requests.put(ENDPOINT + "/create-task",json=payload)