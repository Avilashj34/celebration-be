from fastapi import FastAPI
from backend.api_v0 import api

app = FastAPI() # openapi_url='/api'

app.include_router(
    api.router,
    prefix='/api',
    responses={404: {"description": "Not found"}}
)

