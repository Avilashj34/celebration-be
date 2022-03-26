from fastapi import FastAPI
from api_v0 import api

app = FastAPI() # openapi_url='/api'

app.include_router(api.router, prefix='/api')



