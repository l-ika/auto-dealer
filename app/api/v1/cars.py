from fastapi import APIRouter
from app.services import cars as cars_services


router = APIRouter()

@router.get('/catalog')
def get_all_cars() -> list:
    return cars_services.get_all_cars()