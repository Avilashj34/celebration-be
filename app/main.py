from fastapi import FastAPI
from api import products

app = FastAPI() # openapi_url='/api'

# app.include_router(prefix='/api')
app.include_router(products.router)



