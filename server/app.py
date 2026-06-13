from flask import Flask, jsonify, request
from data import inventory
# from lib.food_api import FoodAPI

app = Flask(__name__)

data = inventory

@app.route("/inventory")
def get_inventory():
    return jsonify(data), 200

if __name__ == "__main__":
    app.run(debug=True)