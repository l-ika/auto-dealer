from datetime import datetime
from decimal import Decimal
from enum import Enum


from pydantic import BaseModel, Field

from app.schemas.car_specifications import CarSpecificationCreateSchema
from app.schemas.car_specifications import CarSpecificationResponseSchema

class BodyTypeEnum(str, Enum):
    SEDAN = 'Седан'
    STATION_WAGON = 'Универсал'
    SUV = 'Внедорожник'
    HATCHBACK = 'Хэтчбек' 

def get_current_year():
    return datetime.now().year

class CarCreateSchema(BaseModel):
    make: str = Field(..., max_length=50)
    model: str = Field(..., max_length=50)
    year_produced: int = Field(get_current_year(), gt=1800, lt=get_current_year()+1)
    country: str = Field(..., max_length=50)
    price: float = Field(..., gt=0)
    body_type: BodyTypeEnum = Field(BodyTypeEnum.SEDAN, max_length=15)
    description: str | None = Field(None, max_length=300)
    specifications: CarSpecificationCreateSchema | None = Field(...)


class CarResponseSchema(BaseModel):
    id: int
    make: str
    model: str
    year_produced: int
    country: str
    price: Decimal
    body_type: str
    description: str | None
    specifications: CarSpecificationResponseSchema | None = None

    model_config = {
        'from_attributes': True
    }