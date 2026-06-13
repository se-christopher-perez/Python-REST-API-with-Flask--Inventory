from flask import Flask, jsonify, request
from data import inventory
# from lib.food_api import FoodAPI

app = Flask(__name__)

data = inventory

@app.route("/inventory")
def get_inventory():
    return jsonify(data), 200

@app.route("/inventory/<int:id>")
def get_product(id):
    found_product = next((item for item in data if item["id"] == id), None)

    if found_product:
        return jsonify(found_product), 200
    
    return jsonify({"error": "Product not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)