from datetime import date

from sqlalchemy import Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class TariffDateTable(Base):
    __tablename__ = "tariff_dates"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    date: Mapped[date] = mapped_column(Date, nullable=False, unique=True)

    tariffs = relationship("TariffTable", back_populates="tariff_date")


class TariffTable(Base):
    __tablename__ = "tariffs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    date_id: Mapped[int] = mapped_column(Integer, ForeignKey("tariff_dates.id"), nullable=False)
    cargo_type: Mapped[str] = mapped_column(String, nullable=False)
    rate: Mapped[float] = mapped_column(Float, nullable=False)

    tariff_date = relationship("TariffDateTable", back_populates="tariffs")
