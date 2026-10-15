from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.repository import cars as cars_repository
from app.schemas.cars import CarCreateSchema


def get_all_cars(db: Session) -> list:
    cars = cars_repository.get_all_cars(db)
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