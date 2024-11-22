from datetime import date

from pydantic import BaseModel, Field, confloat


class Tariff(BaseModel):
    cargo_type: str
    rate: confloat(ge=0)


class TariffDate(BaseModel):
    data: dict[date, list[Tariff]] = Field(examples=[
        {
            "2020-06-01": [
                {
                    "cargo_type": "string",
                    "rate": 0.0
                },
                {
                    "cargo_type": "string",
                    "rate": 0.0
                }
            ],
            "2020-07-01": [
                {
                    "cargo_type": "string",
                    "rate": 0.0
                },
                {
                    "cargo_type": "string",
                    "rate": 0.0
                }
            ]
        }
    ])
