import requests
import lesson8.conftest

def test_role_created3(app_url, role_data):
    print("\nBook:", role_data["book"])
    role_data["level"] = ""
    response = requests.post(app_url + "roles/", data=role_data)
    assert response.status_code == 201
    role_data['id']=response.json()['id']
    assert response.json()!=role_data