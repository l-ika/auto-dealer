from sqlalchemy.orm import Session
from app.models.cars import Car
from app.schemas.cars import CarCreateSchema


def get_all_cars(db: Session, make: str | None = None) -> list[Car]:
    if make is None:
        return db.query(Car).all()
    return db.query(Car).filter(Car.make == make).all()

def add_new_car(db: Session, item: CarCreateSchema) -> Car:
    car = Car(**item.model_dump())
    db.add(car)
    db.commit()
    db.refresh(car)
    return car

def edit_car(db: Session, id: int, item: CarCreateSchema) -> Car | None:
    car = db.query(Car).filter(Car.id == id).first()
    if car is None:
        return None
    new = item.model_dump()
    print(new)
    for key, value in new.items():
        setattr(car, key, value)
    db.commit()
    db.refresh(car)
    return car

def update_car_price(db: Session, id: int, price: float) -> Car | None:
    car = db.query(Car).filter(Car.id == id).first()
    if car is None:
        return None
    car.price = price
    db.commit()
    db.refresh(car)
    return car