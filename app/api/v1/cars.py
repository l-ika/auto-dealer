from decimal import Decimal

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.cars import CarCreateSchema, CarResponseSchema
from app.services import cars as cars_services
from dependency import get_db


router = APIRouter()

@router.get('/catalog', response_model=list[CarResponseSchema])
def get_cars_by_make(make: str | None = None, db: Session = Depends(get_db)) -> list:
    return cars_services.get_all_cars(db, make=make) 

@router.post('/cars/new')
def add_new_car(item: CarCreateSchema, db: Session = Depends(get_db)) -> dict:
    return cars_services.add_new_car(db, item)

@router.put('/cars/edit')
def edit_car(item: CarCreateSchema, db: Session = Depends(get_db)) -> dict:
    return {
        'message' : '...'
    }

@router.patch('/cars/{id}')
def update_car_price(id: int, price: float, db: Session = Depends(get_db)) -> dict:
    return cars_services.update_car_price(db, id, price)