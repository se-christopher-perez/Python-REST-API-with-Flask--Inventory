# Python-REST-API-with-Flask--Inventory

## Summary
You have been hired by a small retail company to develop an inventory management system. This system will allow employees to add, edit, view, and delete inventory items. Additionally, the system will fetch real-time product data from an external API (e.g., OpenFoodFacts API) to supplement product details.

## Functionality
- A Flask-based REST API with CRUD operations for managing inventory

- An external API integration to fetch product details by barcode or name

- A CLI-based interface to interact with the API

- Unit tests to validate functionality and interactions

## Tools Used
- Python

- Flask

- Pytest

- Requests

- Development Tools: A text editor or IDE (e.g., VS Code), browser developer tools, and GitHub

- OpenFoodFacts API

## Installation
- Clone the repo

- Install dependencies: pipenv install, pipenv shell

## How to Run
- Start the Flask server: python3 server/app.py

- Run the CLI (in a second terminal): python3 cli.py

- Run the tests: pytest testing/app_test.py

## File Structure
```
root
├── cli.py
├── server
│   ├── app.py
│   ├── data.py
│   └── food_api.py
└── testing
    └── app_test.py
```

## API Endpoints
- GET - /inventory - Fetch all products

- GET - `/inventory/<id>` - Fetch a product

- POST - /inventory - Add a new product

- PATCH - `/inventory/<id>` - Update a product

- DELETE - `/inventory/<id>` - Delete a product

- GET - `/inventory/search/<barcode>` - Use OpenFood API and search by barcode number

## CLI Commands
- get_all() - View all inventory

- get_product(id) - View single item

- add_new_product() - Add a product

- update_product(id, price, stock) - Update price and stock

- delete_product(id) - Delete a product

- search_barcode(barcode) - Search OpenFoodFacts
