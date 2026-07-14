import requests
from dotenv import load_dotenv
import os


load_dotenv()
base_url = 'https://ru.yougile.com/api-v2'
token = os.getenv("YOUGILE_TOKEN", "")
HEADERS = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}


def test_new_project_pos():
    project_1 = {
        "title": "first"
    }
    resp = requests.post(base_url + '/projects',
                         json=project_1, headers=HEADERS)
    assert resp.status_code in [200, 201]
    assert "id" in resp.json()


def test_new_project_negative():
    project_2 = {
        "title": ""
    }
    resp = requests.post(base_url + '/projects',
                         json=project_2, headers=HEADERS)
    assert resp.status_code in [400]
