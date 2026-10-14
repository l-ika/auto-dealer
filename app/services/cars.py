from fastapi import HTTPException
from app.repository import cars as cars_repository


def get_all_cars() -> list:
    cars = cars_repository.get_all_cars()
    if not len(cars):
        raise HTTPException(
            status_code=400,
            detail=f'No cars in list'
        )
    return cars