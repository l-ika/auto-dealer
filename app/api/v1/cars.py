from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.cars import CarCreateSchema, CarResponseSchema
from app.services import cars as cars_services
from dependency import get_db


router = APIRouter()

@router.get('/catalog', response_model=list[CarResponseSchema])
def get_all_cars(db: Session = Depends(get_db)) -> list:
    return cars_services.get_all_cars(db)

@router.post('/cars/new')
def add_new_car(item: CarCreateSchema, db: Session = Depends(get_db)):
    pass