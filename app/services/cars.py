from decimal import Decimal

from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.repository import cars as cars_repository
from app.schemas.cars import CarCreateSchema


def get_all_cars(db: Session, make: str | None = None) -> list:
    cars = cars_repository.get_all_cars(db, make=make)
    if not len(cars):
        raise HTTPException(
            status_code=400,
            detail=f'No cars in list'
        )
    return cars

def add_new_car(db: Session, item: CarCreateSchema) -> dict:
    car = cars_repository.add_new_car(db, item)
    return {
        'id' : car.id,
        'make' : car.make,
        'model' : car.model,
        'year' : car.year_produced,
        'message' : 'Saving successful'
    }

def edit_car(db: Session, id: int, item: CarCreateSchema) -> dict:
    car = cars_repository.edit_car(db, id, item)
    if car is None:
        raise HTTPException(
            status_code=400,
            detail=f'Car not found'
        )
    return {
        'id' : car.id,
        'make' : car.make,
        'model' : car.model,
        'year' : car.year_produced,
        'price' : car.price,
        'message' : 'Updating successful'
    }

def update_car_price(db: Session, id: int, price: float) -> dict:
    car = cars_repository.update_car_price(db, id,  price)
    if car is None:
        raise HTTPException(
            status_code=400,
            detail=f'Car not found'
        )
    return {
        'id' : car.id,
        'make' : car.make,
        'model' : car.model,
        'year' : car.year_produced,
        'price' : car.price,
        'message' : 'Updating successful'
    }

def delete_car(db: Session, id: int) -> dict:
    is_deleted = cars_repository.delete_car(db, id)
    if not is_deleted:
        raise HTTPException(
            status_code=400,
            detail=f'Car not found'
        )
    return {
        'message' : f'Car with id = {id} has been deleted'
    }