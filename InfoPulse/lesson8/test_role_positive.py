import requests
import pytest
import sys

skipwin = pytest.mark.skipif(sys.platform.startswith("win") is True, reason="Platform Windows")

# @skipwin
def test_role_created(app_url, role_data):
    print("\nBook:", role_data["book"])
    response = requests.post(app_url + "roles/", data=role_data)
    assert response.status_code == 201

# @skipwin
def test_role_created2(app_url, role_data):
    print("\nBook:", role_data["book"])
    role_data["level"] = 1
    response = requests.post(app_url + "roles/", data=role_data)
    assert response.status_code == 201
