from fastapi import HTTPException, status

DateNotFoundException = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="Date id not found."
)

TariffNotFoundException = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Tariff id not found."
)
