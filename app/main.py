from fastapi import FastAPI
from app.routers import products

app = FastAPI()

# Register routers
app.include_router(products.router)
