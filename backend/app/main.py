from fastapi import FastAPI
from .database import init_db
from .config import settings
from .routers import auth as auth_router, products as products_router, orders as orders_router, ai as ai_router

app = FastAPI(title=settings.PROJECT_NAME)

@app.on_event("startup")
def on_startup():
    init_db()

app.include_router(auth_router.router)
app.include_router(products_router.router)
app.include_router(orders_router.router)
app.include_router(ai_router.router)

@app.get("/")
def root():
    return {"message": "E-commerce backend up. Use /docs for swagger UI"}
