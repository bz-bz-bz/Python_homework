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


def test_get_id():
    create_project = {
        "title": "Get ID project"
    }
    create_resp = requests.post(base_url + '/projects',
                                json=create_project, headers=HEADERS)
    project_id = create_resp.json()["id"]
    resp = requests.get(base_url + f'/projects/{project_id}', headers=HEADERS)
    assert resp.status_code == 200
    assert resp.json().get("id") == project_id
    assert resp.json().get("title") == "Get ID project"


def test_get_id_negative():
    invalid_id = "00000000-0000-0000-0000-000000000000"
    resp = requests.get(base_url + f'/projects/{invalid_id}', headers=HEADERS)
    assert resp.status_code == 404
