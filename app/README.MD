# Unisport Product FastAPI

A simple RESTful API for managing (CRUD) a product catalog, built with FastAPI. This API allows users to create, read, update, and delete products, making it easy to manage a sports-related product database.

## Table of Contents

- [Features](#features)
- [Technologies](#technologies)
- [Reasoning](#reasoning)
- [Getting Started](#getting-started)
- [Endpoints](#endpoints)

## Features

- Create a new product
- Retrieve a list of products with pagination
- Get detailed information about a specific product
- Update existing product details
- Delete a product from the catalog

## Technologies

- [Python 3.8+](https://www.python.org/downloads/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Pydantic](https://pydantic-docs.helpmanual.io/)
- [pytest](https://docs.pytest.org/en/latest/)
- [httpx](https://www.python-httpx.org/)

## Reasoning
For developing this API we started with a common framework for developing an Python API (FastAPI), with this settled the next choice was on how to handle the unisport catalog supplied, and they have been used as a dictionary to make and thus we end up with a simple to use and responsive CRUD.
## Getting Started

### For running

1. Python 3.8 or later installed on your machine.
2. Run uvicorn with the following command (8080 can be changed with desired port)
```
uvicorn app.main:app --port 8080 --reload
```

### For testing
Run the following command
```
pytest tests/tests.py
```
## Endpoints
### POST /products/
This endpoint creates a new endpoint in the database with the following structure
```
{
    "id": "1",
    "product_id": 101,
    "style": "Casual T-Shirt",
    "prices": {
        "currency": "USD",
        "min_price": "19.99",
        "max_price": "29.99",
        "recommended_retail_price": "24.99",
        "discount_percentage": "20"
    },
    "name": "Sporty Casual Tee",
    "brand": "ActiveWear",
    "relative_url": "/products/sporty-casual-tee",
    "image": "https://example.com/images/sporty-casual-tee.jpg",
    "delivery": "2-4 days",
    "online": true,
    "active": true,
    "labels": [
        {
            "id": 1,
            "name": "New",
            "priority": 1,
            "color": "green",
            "background_color": "lightgreen",
            "active": true
        }
    ],
    "is_customizable": false,
    "paid_print": false,
    "is_exclusive": false,
    "stock": [
        {
            "pk": 1,
            "sku_id": 201,
            "size_id": 301,
            "barcode": "0123456789012",
            "order_by": 1,
            "name": "M",
            "name_short": "Medium",
            "stock_info": "In stock",
            "price": "19.99",
            "recommended_retail_price": "24.99",
            "discount_percentage": "20",
            "supplier": "ActiveSupplies",
            "is_marketplace": false,
            "delivery": {
                "min_days": 2,
                "max_days": 4,
                "delivery_string": "Standard Shipping"
            },
            "availability": "Available"
        }
    ],
    "currency": "USD",
    "url": "https://example.com/products/sporty-casual-tee",
    "attributes": {
        "club_national": null,
        "boot_with_sock": "No",
        "boot_material": "Cotton",
        "boot_model": "Sporty",
        "segment": "Apparel",
        "brand": "ActiveWear",
        "boot_collection": "Summer Collection",
        "pricepoint": "Affordable",
        "position": ["front", "back"],
        "boot_benefit": "Comfortable",
        "players": [],
        "boot_surface": [],
        "gender": ["Men", "Women"],
        "item_type": "Shirt",
        "age": ["Adult"],
        "quarter": "Q4",
        "color": ["Blue", "White"],
        "sort_date": "2024-10-01",
        "brand_collection": "ActiveWear Collection",
        "warehouse_customization_color": "N/A"
    }
}
```
### GET /products/
Returns the first 10 cheapest products if no page value is given, if a page is given returns the 10 cheapest products using pagination

### GET /products/{product_id}
Gets one specific product based on the product id 

### PUT /products/{product_id}
Updates one specific product based on earlier structure

### DELETE /products/{product_id}
Delete one specific product based on earlier structure