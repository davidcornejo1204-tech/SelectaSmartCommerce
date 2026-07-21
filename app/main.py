from fastapi import FastAPI
from fastapi.routing import APIRoute
from sqlalchemy import text

from app.core.database import engine

from app.routers.brands import router as brands_router
from app.routers.categories import router as categories_router
from app.routers.products import router as products_router

print("=" * 60)
print("ESTOY EJECUTANDO ESTE main.py")
print(__file__)
print("=" * 60)

app = FastAPI(
    title="Selecta Smart Commerce",
    version="0.1.0",
)

app.include_router(brands_router)
app.include_router(categories_router)
app.include_router(products_router)

print("=== RUTAS REGISTRADAS ===")
for route in app.routes:
    if isinstance(route, APIRoute):
        print(route.path)


@app.get("/")
def root():
    return {
        "application": "Selecta Smart Commerce",
        "status": "online",
        "version": "0.1.0",
        "company": "La Selecta Droguería",
    }


@app.get("/database")
def database_test():
    with engine.connect() as connection:
        version = connection.execute(
            text("SELECT version();")
        ).scalar()

    return {
        "database": "connected",
        "postgres_version": version,
    }