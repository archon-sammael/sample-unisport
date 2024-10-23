from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.product import ProductModel
from app.db.db import load_products_from_file

router = APIRouter()

# In-memory database for simplicity
FILE_PATH = "app/catalog/unisport_products.json"

# Load products from the file at the start
products_db = load_products_from_file(FILE_PATH)


# Create product
@router.post("/products/", response_model=ProductModel)
def create_product(product: ProductModel):
    # Check if product already exists
    for db_product in products_db:
        if db_product.product_id == product.product_id:
            raise HTTPException(status_code=400, detail="Product already exists")

    products_db.append(product)
    return product


# Read all products
@router.get("/products/", response_model=List[ProductModel])
def get_products(page: int = 1):
    page_size = 10
    # Sort products by the minimum price
    sorted_products = sorted(products_db, key=lambda product: float(product['prices']['min_price']))

    # Calculate the start and end index for pagination
    start = (page - 1) * page_size
    end = start + page_size

    # Get the products for the requested page
    paginated_products = sorted_products[start:end]

    # Check if the requested page is valid
    if not paginated_products:
        raise HTTPException(status_code=404, detail="No products found on this page")

    return paginated_products


# Read a single product by product_id
@router.get("/products/{product_id}", response_model=ProductModel)
def get_product(product_id: int):
    for product in products_db:
        if product['product_id'] == product_id:  # Use dictionary key access
            return product
    raise HTTPException(status_code=404, detail="Product not found")


# Update product
@router.put("/products/{product_id}", response_model=ProductModel)
def update_product(product_id: int, updated_product: ProductModel):
    for index, product in enumerate(products_db):
        if product.product_id == product_id:
            products_db[index] = updated_product
            return updated_product
    raise HTTPException(status_code=404, detail="Product not found")


# Delete product
@router.delete("/products/{product_id}", response_model=dict)
def delete_product(product_id: int):
    for index, product in enumerate(products_db):
        if product.product_id == product_id:
            products_db.pop(index)
            return {"message": "Product deleted successfully"}
    raise HTTPException(status_code=404, detail="Product not found")
