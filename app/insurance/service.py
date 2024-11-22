from datetime import date

from sqlalchemy import select, insert, delete, update
from sqlalchemy.exc import SQLAlchemyError

from app.database import async_session_maker
from app.exceptions import DateNotFoundException, TariffNotFoundException
from app.insurance.models import TariffDateTable, TariffTable


class TariffService:

    @staticmethod
    async def create_date(tariff_date: date):
        async with async_session_maker() as session:
            try:
                query = (insert(TariffDateTable)
                         .values(date=tariff_date)
                         .returning(TariffDateTable.id)
                         )
                result = await session.execute(query)
                await session.commit()
                new_date_id = result.scalar_one()
                return new_date_id

            except SQLAlchemyError as e:
                await session.rollback()
                raise Exception(f"Database error in create_date: {e}")

    @staticmethod
    async def get_date_id(tariff_date: date):
        async with async_session_maker() as session:
            query = select(TariffDateTable).filter_by(date=tariff_date)
            result = await session.execute(query)
            date_entry = result.scalars().first()

            if not date_entry:
                return None

            return date_entry.id

    @staticmethod
    async def create_tariff(date_id, cargo_type, rate):
        async with async_session_maker() as session:
            query = insert(TariffTable).values(
                date_id=date_id,
                cargo_type=cargo_type,
                rate=rate
            ).returning(TariffTable)

            new_tariff = await session.execute(query)
            await session.commit()
            return new_tariff.scalar()

    @staticmethod
    async def get_cargo_rate(cargo_type, tariff_date):
        async with async_session_maker() as session:
            date_id = await TariffService.get_date_id(tariff_date=tariff_date)

            if not date_id:
                raise DateNotFoundException

            query = select(TariffTable).filter_by(date_id=date_id, cargo_type=cargo_type)
            result = await session.execute(query)
            rate = result.scalars().first()

            if not rate:
                raise ValueError(f"No rate found for cargo type {cargo_type} on {tariff_date}")

            return rate.rate

    @staticmethod
    async def delete_tariff_by_id(tariff_id: int):
        async with async_session_maker() as session:
            query = delete(TariffTable).where(TariffTable.id == tariff_id)
            result = await session.execute(query)

            if not result.rowcount:
                raise TariffNotFoundException

            await session.commit()
            return {"detail": f"Tariff with ID {tariff_id} successfully deleted."}

    @staticmethod
    async def update_tariff(tariff_id, new_date, new_cargo_type, new_rate):
        async with async_session_maker() as session:
            get_tariff = select(TariffTable).filter_by(id=tariff_id)
            tariff_obj = await session.execute(get_tariff)
            tariff = tariff_obj.scalars().first()

            if not tariff:
                raise TariffNotFoundException

            new_date_id = await TariffService.get_date_id(tariff_date=new_date)

            if not new_date_id:
                new_date_id = await TariffService.create_date(tariff_date=new_date)

            query = (
                update(TariffTable)
                .where(TariffTable.id == tariff_id)
                .values(date_id=new_date_id,
                        cargo_type=new_cargo_type,
                        rate=new_rate)
            )

            await session.execute(query)
            await session.commit()

            return {"detail": "tariff successfully updated"}
