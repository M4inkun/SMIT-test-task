from fastapi import FastAPI

from app.insurance.router import router as router_insurance

app = FastAPI()

app.include_router(router_insurance)
