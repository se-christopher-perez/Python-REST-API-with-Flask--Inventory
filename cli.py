import requests

URL = "http://127.0.0.1:5000"

def get_all():
    response = requests.get(f"{URL}/inventory")
    products = response.json()

    for product in products:
        print(product)

get_all()

def get_product(id):
    response = requests.get(f"{URL}/inventory/{id}")
    print(response.json())

get_product(2)