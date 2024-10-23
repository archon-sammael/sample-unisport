import json


# Initialize products_db from a JSON file
def load_products_from_file(file_path: str):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)["products"]
    except FileNotFoundError:
        return []  # Return an empty list if the file doesn't exist
