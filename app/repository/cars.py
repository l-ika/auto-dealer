from sqlalchemy.orm import Session
from app.models.cars import Car
from app.schemas.cars import CarCreateSchema


def get_all_cars(db: Session) -> list[Car]:
    return db.query(Car).all()

def add_new_car(db: Session, item: CarCreateSchema) -> Car:
    car = Car(**item.model_dump())
    db.add(car)
    db.commit()
    db.refresh(car)
    return car