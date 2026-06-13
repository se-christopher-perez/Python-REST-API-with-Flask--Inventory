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

def add_new_product(product_name, brands, ingredients, quantity, price, stock):
    response = requests.post(f"{URL}/inventory", json={
        
        "product_name": product_name,
        "brands": brands,
        "ingredients": ingredients,
        "quantity": quantity,
        "price": price,
        "stock": stock
    
    })

    print(response.json())

add_new_product("Oreos", "Nabisco", "Sugar, flour, cocoa", "154g", 2.99, 30)

def update_product(id, price, stock):
    response = requests.patch(f"{URL}/inventory/{id}", json={
    
        "price": price,
        "stock": stock

    })

    print(response.json())

update_product(3, 29.99, 100)

def delete_product(id):
    response = requests.delete(f"{URL}/inventory/{id}")

    print(response.json())

delete_product(1)

def search_barcode(barcode):
    response = requests.get(f"{URL}/inventory/search/{barcode}")

    print(response.json())

search_barcode("3017620422003")