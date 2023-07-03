ENDPOINT ="https://todo.pixegami.io/"
import requests
response = requests.get(ENDPOINT)
print(response)
data = response.json()
print(data)
status_code=response.status_code
print(status_code)


def new_task_payload():
    return {
        "content":"my test content",
        "user_id": "test_user",
        "is_done": False
    }
