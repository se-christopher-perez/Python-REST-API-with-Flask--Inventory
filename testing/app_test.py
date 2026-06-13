import pytest
import sys
sys.path.append('server')
from app import app

app_test = app.test_client()

def test_get_inventory():
    response = app_test.get("/inventory")

    if response.status_code != 200:
        return TypeError(f"error: {response.status_code}")

    
