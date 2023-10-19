# Import necessary modules and packages
from fastapi import FastAPI
from .import models
from .database import engine
from .routers import product, seller, login



# Create a FastAPI application
app = FastAPI(
    
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
app.include_router(seller.router)
app.include_router(login.router)


# Create database tables if they don't exist
models.Base.metadata.create_all(engine)







