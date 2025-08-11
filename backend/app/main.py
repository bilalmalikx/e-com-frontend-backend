from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import init_db
from .config import settings
from .routers import auth as auth_router, products as products_router, orders as orders_router, ai as ai_router

app = FastAPI(title=settings.PROJECT_NAME)

# ✅ CORS setup so Angular can call FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # ya "*" for all origins (dev purpose)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    init_db()

# ✅ Routers
app.include_router(auth_router.router)
app.include_router(products_router.router)
app.include_router(orders_router.router)
app.include_router(ai_router.router)

# ✅ Root endpoint
@app.get("/")
def root():
    return {"message": "E-commerce backend up. Use /docs for swagger UI"}
