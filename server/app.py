from flask import Flask, jsonify, request
from data import inventory
# from lib.food_api import FoodAPI

app = Flask(__name__)

@app.route("/inventory", methods=["GET"])
def get_inventory():
    return jsonify(inventory), 200

@app.route("/inventory/<int:id>", methods=["GET"])
def get_product(id):
    found_product = next((item for item in inventory if item["id"] == id), None)

    if found_product:
        return jsonify(found_product), 200
    
    return jsonify({"error": "Product not found"}), 404

@app.route("/inventory", methods=["POST"])
def add_product():
    data = request.get_json()

    new_product = {
    
        "id": len(inventory) + 1,
        "product_name": data["product_name"],
        "brands": data["brands"],
        "ingredients": data["ingredients"],
        "quantity": data["quantity"],
        "price": data["price"],
        "stock": data["stock"]
    
    }

    inventory.append(new_product)

    return jsonify(new_product), 201

@app.route("/inventory/<int:id>", methods=["PATCH"])
def update_product(id):
    found_product = next((item for item in inventory if item["id"] == id), None)

    if found_product:
        data = request.get_json()
        found_product.update(data)
        return jsonify(found_product), 200
    return jsonify({"error": "Product not found"}), 404

@app.route("/inventory/<int:id>", methods=["DELETE"])
def delete_product

if __name__ == "__main__":
    app.run(debug=True)