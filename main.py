from fastapi import FastAPI
from app.api.v1.cars import router as cars_router
from database import Base, engine


app = FastAPI()

app.include_router(cars_router, prefix='/api/v1', tags=['cars'])

Base.metadata.create_all(bind=engine)