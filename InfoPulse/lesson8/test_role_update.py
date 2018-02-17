import requests

def test_role_update(app_url, role_data):
    role_data["name"] = "Hitler"
    response = requests.put(app_url + "roles/", data=role_data)
    assert response.status_code == 405  #NOT ALLOW ALL OK
    print(response.text)
def test_role_id_update(app_url, role_data):
    role_data["name"] = "HitlerDolf"
    response = requests.put(app_url+"roles/"+str(role_data['book'])+"/",data=role_data)
    print((app_url+"roles/"+str(role_data['book'])+"/",role_data))
    print(response.status_code)
    print(response.text)
    assert response.status_code