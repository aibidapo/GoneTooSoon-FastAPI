# Import necessary modules and classes from SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base  # Import the Base object for declarative class definitions
from sqlalchemy.orm import relationship


# Define a SQLAlchemy model for the 'Product' entity
class Product(Base):
    __tablename__ = 'products'  # Name of the database table for this model
    id = Column(Integer, primary_key=True, index=True)  # Unique identifier for the product
    name = Column(String)  # Name of the product (string)
    description = Column(String)  # Description of the product (string)
    price = Column(Integer)  # Price of the product (integer)
    seller_id = Column(Integer, ForeignKey('sellers.id'))  # Foreign key linking to the 'id' column of the 'sellers' table
    seller = relationship("Seller", back_populates='products')  # Define a relationship to the 'Seller' model and specify a back reference


# Define a SQLAlchemy model for the 'Seller' entity
class Seller(Base):
    __tablename__ = 'sellers'  # Name of the database table for this model
    id = Column(Integer, primary_key=True, index=True)  # Unique identifier for the seller
    username = Column(String)  # Username of the seller (string)
    email = Column(String)  # Email of the seller (string)
    password = Column(String)  # Password of the seller (string)
    products = relationship("Product", back_populates='seller')  # Define a relationship to the 'Product' model and specify a back reference

        