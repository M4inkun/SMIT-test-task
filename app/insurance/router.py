from datetime import date

from fastapi import APIRouter, HTTPException, Query

from app.insurance.schemas import TariffDate
from app.insurance.service import TariffService

router = APIRouter(
    prefix="/insurance",
    tags=["insurance"]
)


@router.post('/upload_tariffs')
async def upload_tariffs(data: TariffDate):
    try:
        for tariff_date, list_of_tariffs in data.data.items():
            tariff_date_id = await TariffService.get_date_id(tariff_date)

            if not tariff_date_id:
                tariff_date_id = await TariffService.create_date(tariff_date)

            for tariff in list_of_tariffs:
                await TariffService.create_tariff(tariff_date_id, tariff.cargo_type, tariff.rate)

        return {"message": "Tariffs uploaded successfully."}

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error: {str(e)}")


@router.put('/update_tariff/{tariff_id}')
async def update_tariff(tariff_id: int,
                        new_date: date,
                        new_cargo_type: str,
                        new_rate: float):
    result = await TariffService.update_tariff(tariff_id, new_date, new_cargo_type, new_rate)
    return result


@router.delete('/delete_tariff/{tariff_id}')
async def delete_tariff(tariff_id: int):
    result = await TariffService.delete_tariff_by_id(tariff_id)
    return result


@router.get('/calculate_price')
async def calculate_price(cargo_type: str,
                          tariff_date: date,
                          declared_value: float = Query(0.0, gt=0)):
    cargo_rate = await TariffService.get_cargo_rate(cargo_type, tariff_date)

    cost = declared_value * cargo_rate
    return {
        "declared_value": declared_value,
        "cargo_type": cargo_type,
        "tariff_date": tariff_date,
        "cargo_rate": cargo_rate,
        "insurance_cost": f"{round(cost, 2)}",
    }
