from fastapi import FastAPI, Response, HTTPException
from sqlalchemy.sql.functions import mode 
from fastapi.params import Depends
from sqlalchemy.orm import Session
from .import schemas
from .import models
from .database import engine, SessionLocal
from typing import List
from fastapi import status



app = FastAPI(title="Product App 🧙🏼 '\U0001F913' ")

models.Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal()
    
    try:
        yield db
        
    finally:
        db.close()
    


@app.get('/products', response_model=List[schemas.DisplayProduct])
def products(db: Session = Depends(get_db)):
    products = db.query(models.Product).all()
    return products


@app.delete('/product/{id}')
def delete_product(id, db: Session = Depends(get_db)):
    db.query(models.Product).filter(models.Product.id == id).delete(synchronize_session=False)
    db.commit()
    return {f'Product {id} deleted'}



@app.get('/product/{id}', response_model=schemas.DisplayProduct)
def product(id, response: Response, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == id).first()
    
    if not product:
        raise HTTPException(status_code=404, detail=f"Product {id} not found")
        
    return product
    

@app.put('/products/{id}')
def update_product(id, request:schemas.Product, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == id)
    if not product.first():
        pass
    
    product.update(request.dict())
    db.commit()
    return {f'Product {id} successfully updated'}
        



@app.post('/product', status_code=status.HTTP_201_CREATED)
def add(request:schemas.Product, db: Session = Depends(get_db)):
    new_product = models.Product(name=request.name, description=request.description, price=request.price)
    
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return request



@app.post('/seller')
def create_seller(request:schemas.Seller, db: Session = Depends(get_db)):
    new_seller
    return request
