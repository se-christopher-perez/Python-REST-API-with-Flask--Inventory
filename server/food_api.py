import requests

HEADERS = {
    "User-Agent": "MyApp/1.0 (myapp@example.com)"
}

class FoodAPI:

    def search_barcode(self, barcode):
        response = requests.get(
            f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json",
            headers=HEADERS
        )

        if response.status_code != 200:
            print(f"Error: {response.status_code}")
            return None

        product = response.json()["product"]

        return {
            "product_name": product["product_name"],
            "brands":       product["brands"],
            "ingredients":  product["ingredients_text"],
            "quantity":     product["quantity"]
        }
    
nutella = FoodAPI().search_barcode("3017620422003")
coke = FoodAPI().search_barcode("5449000000996")
ketchup = FoodAPI().search_barcode("0013000006408")

print("Search Result:\n")
print(nutella)
print(coke)
print(ketchup)