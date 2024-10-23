from fastapi import APIRouter, HTTPException
from typing import List, Dict, Any
from app.db.db import load_products_from_file, save_products_to_file

router = APIRouter()

# Load products from the file at the start
FILE_PATH = "app/catalog/unisport_products.json"
products_db: List[Dict[str, Any]] = load_products_from_file(FILE_PATH)


# Create product
@router.post("/products/", response_model=Dict[str, Any])
def create_product(product: Dict[str, Any]):
    for db_product in products_db:
        if db_product['product_id'] == product['product_id']:
            raise HTTPException(status_code=400, detail="Product already exists")

    products_db.append(product)  # Append the new product dictionary
    save_products_to_file(FILE_PATH, products_db)  # Save to file
    return product


# Read all products
@router.get("/products/", response_model=List[Dict[str, Any]])
def get_products(page: int = 1):
    page_size = 10
    # Sort products by the minimum price
    sorted_products = sorted(products_db, key=lambda product: float(product['prices']['min_price']))

    start = (page - 1) * page_size
    end = start + page_size

    paginated_products = sorted_products[start:end]
    if not paginated_products:
        raise HTTPException(status_code=404, detail="No products found on this page")

    return paginated_products


# Read a single product by product_id
@router.get("/products/{product_id}", response_model=Dict[str, Any])
def get_product(product_id: int):
    for product in products_db:
        if product['product_id'] == product_id:
            return product  # Return the product dictionary
    raise HTTPException(status_code=404, detail="Product not found")


# Update product
@router.put("/products/{product_id}", response_model=Dict[str, Any])
def update_product(product_id: int, updated_product: Dict[str, Any]):
    for index, product in enumerate(products_db):
        if product['product_id'] == product_id:
            products_db[index] = updated_product  # Update with the new product dictionary
            save_products_to_file(FILE_PATH, products_db)  # Save to file
            return updated_product
    raise HTTPException(status_code=404, detail="Product not found")


# Delete product
@router.delete("/products/{product_id}", response_model=dict)
def delete_product(product_id: int):
    for index, product in enumerate(products_db):
        if product['product_id'] == product_id:
            products_db.pop(index)
            save_products_to_file(FILE_PATH, products_db)  # Save to file
            return {"message": "Product deleted successfully"}
    raise HTTPException(status_code=404, detail="Product not found")