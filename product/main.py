# Import necessary modules and packages
from fastapi import FastAPI, Response, HTTPException
from sqlalchemy.sql.functions import mode
from fastapi.params import Depends
from sqlalchemy.orm import Session
from .import schemas
from .import models
from .database import engine, SessionLocal
from typing import List
from fastapi import status
from passlib.context import CryptContext



# Create a FastAPI application
app = FastAPI(
    
    title="GoneTooSoon Deals🧙🏼 '\U0001F913' "
    description = "Get information about awesome deals FAST!"
    )



# Create database tables if they don't exist
models.Base.metadata.create_all(engine)

# Initialize a password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# Define a function to get a database session using context manager
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Define a route to get a list of products
@app.get('/products', response_model=List[schemas.DisplayProduct])
def products(db: Session = Depends(get_db)):
    products = db.query(models.Product).all()
    return products



# Define a route to delete a product by its ID
@app.delete('/product/{id}')
def delete_product(id, db: Session = Depends(get_db)):
    db.query(models.Product).filter(models.Product.id == id).delete(synchronize_session=False)
    db.commit()
    return {f'Product {id} deleted'}



# Define a route to get a product by its ID
@app.get('/product/{id}', response_model=schemas.DisplayProduct)
def product(id, response: Response, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == id).first()
    if not product:
        raise HTTPException(status_code=404, detail=f"Product {id} not found")
    return product



# Define a route to update a product by its ID
@app.put('/products/{id}')
def update_product(id, request: schemas.Product, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == id)
    if not product.first():
        pass
    product.update(request.dict())
    db.commit()
    return {f'Product {id} successfully updated'}



# Define a route to add a new product
@app.post('/product', status_code=status.HTTP_201_CREATED)
def add(request: schemas.Product, db: Session = Depends(get_db)):
    new_product = models.Product(name=request.name, description=request.description, price=request.price, seller_id=1)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return request



# Define a route to create a new seller
@app.post('/seller', response_model=schemas.DisplaySeller)
def create_seller(request: schemas.Seller, db: Session = Depends(get_db)):
    # Hash the seller's password for security
    hashedpassword = pwd_context.hash(request.password)
    new_seller = models.Seller(username=request.username, email=request.email, password=hashedpassword)
    db.add(new_seller)
    db.commit()
    db.refresh(new_seller)
    return new_seller
