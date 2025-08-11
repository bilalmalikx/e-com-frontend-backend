from sqlmodel import select, Session
from .models import User, Product, Order, OrderItem
from .schemas import ProductCreate, UserCreate, OrderCreate
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Users
def get_user_by_email(session: Session, email: str):
    statement = select(User).where(User.email == email)
    return session.exec(statement).first()

def create_user(session: Session, user_in: UserCreate):
    hashed = pwd_context.hash(user_in.password)
    user = User(email=user_in.email, hashed_password=hashed, full_name=user_in.full_name)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

# Products
def create_product(session: Session, product_in: ProductCreate):
    product = Product.from_orm(product_in)
    session.add(product)
    session.commit()
    session.refresh(product)
    return product

def list_products(session: Session, skip: int = 0, limit: int = 100):
    statement = select(Product).offset(skip).limit(limit)
    return session.exec(statement).all()

def get_product(session: Session, product_id: int):
    statement = select(Product).where(Product.id == product_id)
    return session.exec(statement).first()

# Orders
def create_order(session: Session, order_in: OrderCreate):
    total = 0.0
    order = Order(user_id=order_in.user_id)
    session.add(order)
    session.commit()
    session.refresh(order)
    for item in order_in.items:
        product = get_product(session, item.product_id)
        if not product:
            continue
        price = product.price
        oi = OrderItem(order_id=order.id, product_id=product.id, quantity=item.quantity, price_at_purchase=price)
        session.add(oi)
        total += price * item.quantity
    order.total = total
    session.add(order)
    session.commit()
    session.refresh(order)
    return order
