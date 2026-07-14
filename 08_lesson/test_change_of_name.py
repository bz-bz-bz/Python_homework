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


def test_edit_positive():
    create_project = {
        "title": "Project"
    }
    create_resp = requests.post(base_url + '/projects',
                                json=create_project, headers=HEADERS)
    project_id = create_resp.json()["id"]
    edit_name = {
        "title": "Edit project"
    }
    resp = requests.put(base_url + f'/projects/{project_id}',
                        json=edit_name, headers=HEADERS)
    assert resp.status_code in [200, 201]
    assert resp.json().get("id") == project_id


def test_negative():
    create_project = {
        "title": "Negative"
    }
    create_resp = requests.post(base_url + '/projects',
                                json=create_project, headers=HEADERS)
    project_id = create_resp.json()["id"]
    edit_name = {
        "title": ""
    }
    resp = requests.put(base_url + f'/projects/{project_id}',
                        json=edit_name, headers=HEADERS)
    assert resp.status_code in [400]
