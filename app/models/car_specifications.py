from sqlalchemy import CheckConstraint, ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base


class CarSpecification(Base):
    __tablename__ = 'car_specifications'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    car_id: Mapped[int] = mapped_column(
        ForeignKey('cars.id', ondelete='CASCADE', onupdate='CASCADE'),
        unique=True
        ) 
    fuel_type: Mapped[str] = mapped_column(String(10), default='Бензин')
    engine_volume: Mapped[float] = mapped_column(Numeric(2, 1))
    drive_type: Mapped[str] = mapped_column(String(10), default='Передний')
    transmission: Mapped[str] = mapped_column(String(15), default='Механическая')
    horsepower: Mapped[int] = mapped_column(Integer)

    car = relationship('Car', uselist=False, back_populates='specifications')

    __table_args__ = (
        CheckConstraint (
            "fuel_type IN ('Бензин', 'Дизель', 'Электро', 'Гибрид')",
            name='fuel_type_check'
        ),
        CheckConstraint (
            "drive_type IN ('Передний', 'Задний', 'Полный')",
            name='drive_type_check'
        ),
        CheckConstraint (
            "transmission IN ('Автоматическая', 'Механическая', 'Робот', 'Вариатор')",
            name='transmission_check'
        ),
        CheckConstraint (
            "engine_volume >= 0",
            name='engine_volume_not_negative'
        ),
        CheckConstraint (
            "horsepower > 0",
            name='horsepower_is_positive'
        )
    )

    def __str__(self) -> str:
        return f"""
            id: {self.id}
            car_id: {self.car_id}
            fuel_type: {self.fuel_type}
            engine_volume: {self.engine_volume}
            drive_type: {self.drive_type}
            transmission: {self.transmission}
            horsepower: {self.horsepower}
        """