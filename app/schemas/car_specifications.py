from enum import Enum

from pydantic import BaseModel, Field

class FuelTypeEnum(str, Enum):
    GAS = 'Бензин'
    DIESEL = 'Дизель'
    ELECTRIC = 'Электро'
    HYBRID = 'Гибрид'

class DriveTypeEnum(str, Enum):
    FWD = 'Передний'
    RWD = 'Задний'
    AWD = 'Полный'

class TransmissionEnum(str, Enum):
    AUTOMATIC = 'Автоматическая'
    MANUAL = 'Механическая'
    ROBOT = 'Робот'
    CVT = 'Вариатор'

class CarSpecificationCreateSchema(BaseModel):
    fuel_type: FuelTypeEnum = Field(FuelTypeEnum.GAS, max_length=10)
    engine_volume: float = Field(..., ge=0)
    drive_type: DriveTypeEnum = Field(DriveTypeEnum.FWD, max_length=10)
    transmission: TransmissionEnum = Field(TransmissionEnum.MANUAL, max_length=15)
    horsepower: int = Field(..., gt=0)

class CarSpecificationResponseSchema(BaseModel):
    id: int
    car_id: int
    fuel_type: str
    engine_volume: float
    drive_type: str
    transmission: str
    horsepower: int

    model_config = {
            'from_attributes': True
        }
    