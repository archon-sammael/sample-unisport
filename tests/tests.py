from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_product():
    new_product = {
        "id": "1",
        "product_id": 101,
        "style": "Sneakers",
        "prices": {
            "currency": "USD",
            "min_price": "19.99",
            "max_price": "29.99",
            "recommended_retail_price": "25.00",
            "discount_percentage": "20"
        },
        "name": "Sport Sneakers",
        "brand": "BrandX",
        "relative_url": "/products/101",
        "image": "http://example.com/image.png",
        "delivery": "Fast",
        "online": True,
        "active": True,
        "labels": [],
        "is_customizable": False,
        "paid_print": False,
        "is_exclusive": False,
        "stock": [],
        "currency": "USD",
        "url": "http://example.com/products/101",
        "attributes": {
            "club_national": None,
            "boot_with_sock": "No",
            "boot_material": "Mesh",
            "boot_model": "ModelX",
            "segment": "Sports",
            "brand": "BrandX",
            "boot_collection": "CollectionX",
            "pricepoint": "Budget",
            "position": [],
            "boot_benefit": "Comfort",
            "players": [],
            "boot_surface": [],
            "gender": ["Unisex"],
            "item_type": "Footwear",
            "age": ["Adult"],
            "quarter": "Q1",
            "color": ["Red"],
            "sort_date": "2024-01-01",
            "brand_collection": "CollectionY",
            "warehouse_customization_color": "None"
        }
    }

    response = client.post("/products/", json=new_product)
    assert response.status_code == 200
    assert response.json() == new_product


def test_get_products():
    response = client.get("/products/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Ensure it's a list


def test_get_product():
    response = client.get("/products/101")  # Adjust to the existing product ID
    assert response.status_code == 200
    assert response.json()["product_id"] == 101  # Check specific product ID


def test_delete_product():
    response = client.delete("/products/101")  # Adjust to the existing product ID
    assert response.status_code == 200
    assert response.json() == {"message": "Product deleted successfully"}

    # Check if product is really deleted
    response = client.get("/products/101")
    assert response.status_code == 404  # Should not be found
