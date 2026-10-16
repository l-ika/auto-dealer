from sqlalchemy.orm import Session
from app.models.car_specifications import CarSpecification
from app.models.cars import Car
from app.schemas.car_specifications import CarSpecificationCreateSchema
from app.schemas.cars import CarCreateSchema


def get_all_cars(db: Session, make: str | None = None) -> list[Car]:
    if make is None:
        return db.query(Car).all()
    return db.query(Car).filter(Car.make == make).all()


def add_new_car(db: Session, item: CarCreateSchema) -> Car:
    car_data = item.model_dump()
    specifications_data = car_data.pop('specifications', None)

    car = Car(**car_data)
    db.add(car)

    if specifications_data is not None:
        db.flush()
        specifications = CarSpecification(**specifications_data)
        specifications.car_id = car.id 
        db.add(specifications)

    db.commit()
    db.refresh(car)
    return car


def edit_car(db: Session, id: int, item: CarCreateSchema) -> Car | None:
    new_data = item.model_dump()
    new_specifications = new_data.pop('specifications', None)
    car = db.query(Car).filter(Car.id == id).first()
    old_specifications = db.query(CarSpecification).filter(CarSpecification.car_id == id).first()
    
    if car is None:
        return None

    if new_specifications is not None:
        if old_specifications is not None:
            for key, value in new_specifications.items():
                setattr(old_specifications, key, value)
        else:
            car_spec = CarSpecification(**new_specifications)
            car_spec.car_id = id
            db.add(car_spec)
    else:
        if old_specifications is not None:
            db.delete(old_specifications)

    for key, value in new_data.items():
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


def delete_car(db: Session, id: int) -> bool:
    car = db.query(Car).filter(Car.id == id).first()
    if car is None:
        return False
    db.delete(car)
    db.commit()
    return True