import json
from typing import List, Dict, Any


# Initialize products_db from a JSON file
def load_products_from_file(file_path: str) -> List[Dict[str, Any]]:
    with open(file_path, "r") as f:
        return json.load(f)  # This should return a list of products


# Save products to the file
def save_products_to_file(file_path: str, products: List[Dict[str, Any]]):
    with open(file_path, "w") as f:
        json.dump(products, f, indent=4)
