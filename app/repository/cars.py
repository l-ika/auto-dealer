from sqlalchemy.orm import Session
from app.models.cars import Car


def get_all_cars(db: Session) -> list[Car]:
    return db.query(Car).all()