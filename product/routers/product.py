from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi.params import Depends
from ..database  import get_db
from ..import models, schemas
from typing import List
from fastapi import FastAPI, Response, HTTPException
from fastapi import status



router = APIRouter()


# Define a route to get a list of products
@router.get('/products', response_model=List[schemas.DisplayProduct], tags=["Products"])
def products(db: Session = Depends(get_db)):
    products = db.query(models.Product).all()
    return products



# Define a route to delete a product by its ID
@router.delete('/product/{id}', tags=["Products"])
def delete_product(id, db: Session = Depends(get_db)):
    db.query(models.Product).filter(models.Product.id == id).delete(synchronize_session=False)
    db.commit()
    return {f'Product {id} deleted'}



# Define a route to get a product by its ID
@router.get('/product/{id}', response_model=schemas.DisplayProduct, tags=["Products"])
def product(id, response: Response, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == id).first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Product {id} not found")
    return product



# Define a route to update a product by its ID
@router.put('/products/{id}', tags=["Products"])
def update_product(id, request: schemas.Product, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == id)
    if not product.first():
        pass
    product.update(request.dict())
    db.commit()
    return {f'Product {id} successfully updated'}



# Define a route to add a new product
@router.post('/product', status_code=status.HTTP_201_CREATED, tags=["Products"])
def add(request: schemas.Product, db: Session = Depends(get_db)):
    new_product = models.Product(name=request.name, description=request.description, price=request.price, seller_id=1)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return request
