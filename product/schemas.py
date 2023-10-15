# Importing the BaseModel class from Pydantic
from pydantic import BaseModel


# Defining a Pydantic model for the 'Product' entity
class Product(BaseModel):
    # Defining the fields for the 'Product' model
    name: str         # Name of the product (string)
    description: str  # Description of the product (string)
    price: int        # Price of the product (integer)



# Defining a Pydantic model for displaying 'Product' data
class DisplayProduct(BaseModel):
    name: str         # Name of the product (string)
    description: str  # Description of the product (string)
    id: int           # Identifier (ID) of the product (integer)

    # Pydantic model configuration
    class Config:
        orm_mode = True  # Configuring 'orm_mode' to work with SQLAlchemy ORM



# Defining a Pydantic model for the 'Seller' entity
class Seller(BaseModel):
    # Defining the fields for the 'Seller' model
    username: str     # Username of the seller (string)
    email: str        # Email of the seller (string)
    password: str     # Password of the seller (string)
    id: int           # Identifier (ID) of the seller (integer)



# Defining a Pydantic model for displaying 'Seller' data
class DisplaySeller(BaseModel):
    username: str     # Username of the seller (string)
    email: str        # Email of the seller (string)
    id: int           # Identifier (ID) of the seller (integer)

    # Pydantic model configuration
    class Config:
        orm_mode = True  # Configuring 'orm_mode' to work with SQLAlchemy ORM
