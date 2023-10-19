from fastapi import APIRouter
from ..import models, schemas
from sqlalchemy.orm import Session
from fastapi.params import Depends
from ..database  import get_db
from passlib.context import CryptContext


router = APIRouter()



# Initialize a password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Define a route to create a new seller
@router.post('/seller', response_model=schemas.DisplaySeller, tags=["Seller"])
def create_seller(request: schemas.Seller, db: Session = Depends(get_db)):
    # Hash the seller's password for security
    hashedpassword = pwd_context.hash(request.password)
    new_seller = models.Seller(username=request.username, email=request.email, password=hashedpassword)
    db.add(new_seller)
    db.commit()
    db.refresh(new_seller)
    return new_seller