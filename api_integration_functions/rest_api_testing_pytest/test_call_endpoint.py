import requests
from api_integration_functions.rest_api_function_defination.config import *
def test_can_call_endpoint():
    response= requests.get(ENDPOINT)
    assert response.status_code == 200