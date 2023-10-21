from fastapi import APIRouter, Depends, status, HTTPException
from ..import schemas, database, models
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from ..database import get_db


router = APIRouter()

# Initialize a password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.post('/login')
def login(request: schemas.Login, db: Session = Depends(get_db)):
    seller = db.query(models.Seller).filter(models.Seller.username == request.username).first()
    if not seller:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Username not found / invalid username")
    
    if not pwd_context.verify(request.password, seller.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid password")
    
    
    return request
