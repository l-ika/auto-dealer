from fastapi import APIRouter
from app.schemas.cars import CarCreateSchema
from app.services import cars as cars_services


router = APIRouter()

@router.get('/catalog')
def get_all_cars() -> list:
    return cars_services.get_all_cars()

@router.post('/cars/new')
def add_new_car(item: CarCreateSchema):
    pass