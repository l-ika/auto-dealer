from typing import Optional

from sqlalchemy import CheckConstraint, Integer, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base


class Car(Base):
    __tablename__ = 'cars'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    make: Mapped[str] = mapped_column(String(50))
    model: Mapped[str] = mapped_column(String(50))
    year_produced: Mapped[int] = mapped_column(Integer)
    country: Mapped[str] = mapped_column(String(50))
    price: Mapped[float] = mapped_column(Numeric(15, 2))
    body_type: Mapped[str] = mapped_column(String(15), default='Седан')
    description: Mapped[Optional[str]] = mapped_column(String)

    specifications = relationship('CarSpecification', uselist=False, back_populates='car')

    __table_args__ = (
        CheckConstraint (
            'year_produced > 1800 AND year_produced < 2100',
            name='year_produced_check'
        ),
        CheckConstraint (
            'price > 0',
            name='price_is_positive_check'
        ),
        CheckConstraint (
            "body_type IN ('Седан', 'Универсал', 'Внедорожник', 'Хэтчбек')",
            name='body_type_check'
        )  
    )

    def __str__(self) -> str:
        return f'Car: {self.make} {self.model} {self.year_produced} year'