# Import necessary modules and packages
from fastapi import FastAPI, Response, HTTPException
from sqlalchemy.sql.functions import mode
from fastapi.params import Depends
from sqlalchemy.orm import Session
from .import schemas
from .import models
from .database import engine, SessionLocal
from fastapi import status
from passlib.context import CryptContext
from .database  import get_db
from .routers import product



# Create a FastAPI application
app = FastAPI (
    
    title="GoneTooSoon Deals🧙🏼 '\U0001F913' ",
    description = 'Get information about awesome product deals FAST!',
    terms_of_service = 'http://www.google.com/',
    contact= {
        "Developer name": "A. Ibidapo",
        "website": 'http://www.google.com',
        "email": 'contact_me@anytime.com',
    },
    license_info={
        'name': 'Apache Software License',
        'url': 'http://www.google.com'
    },
    # docs_url="/documentation", redoc_url=None # Changes the documentation path to our API
    )

app.include_router(product.router)



# Create database tables if they don't exist
models.Base.metadata.create_all(engine)

# Initialize a password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")




# Define a route to create a new seller
@app.post('/seller', response_model=schemas.DisplaySeller, tags=["Seller"])
def create_seller(request: schemas.Seller, db: Session = Depends(get_db)):
    # Hash the seller's password for security
    hashedpassword = pwd_context.hash(request.password)
    new_seller = models.Seller(username=request.username, email=request.email, password=hashedpassword)
    db.add(new_seller)
    db.commit()
    db.refresh(new_seller)
    return new_seller
