from fastapi import FastAPI
from app.api.v1.cars import router as cars_router


app = FastAPI()

app.include_router(cars_router, prefix='/api/v1', tags=['cars'])