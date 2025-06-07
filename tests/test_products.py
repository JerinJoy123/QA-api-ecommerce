import pytest
import requests

BASE_URL = "https://fakestoreapi.com"

def test_get_products():
    response = requests.get(f"{BASE_URL}/products")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
