import requests
import pytest

BASE_URL = "https://reqres.in/api"

def test_get_all_users():
    response = requests.get(f"{BASE_URL}/users?page=2")
    assert response.status_code == 200
    assert "data" in response.json()

def test_single_user():
    response = requests.get(f"{BASE_URL}/users/2")
    assert response.status_code == 200
    assert response.json()["data"]["id"] == 2
