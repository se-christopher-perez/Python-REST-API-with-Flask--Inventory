import pytest
import sys
sys.path.append('server')
from app import app

app_test = app.test_client()

def test_get_inventory():
    response = app_test.get("/inventory")

    if response.status_code != 200:
        return TypeError(f"error: {response.status_code}")

def test_get_product():
    response = app_test.get("/inventory/1")

    if response.status_code != 200:
        return TypeError(f"error: {response.status_code}")
    
def test_add_product():
    response = app_test.post("/inventory", json={

        "product_name": "Oreos",
        "brands": "Nabisco",
        "ingredients": "Sugar, flour, cocoa...",
        "quantity": "154g",
        "price": 2.99,
        "stock": 30

    })

    if response.status_code != 201:
        return TypeError(f"error: {response.status_code}")
