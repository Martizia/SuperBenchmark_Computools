import os
from datetime import datetime

from dotenv import load_dotenv
from fastapi import APIRouter, FastAPI, HTTPException

from .database import DatabaseHandler
from .models import AveragePerformance

load_dotenv()

app = FastAPI(title="SuperBenchmark")
router = APIRouter(prefix="/results", tags=["Average"])


DEBUG = os.getenv("SUPERBENCHMARK_DEBUG", "False").lower() == "true"


@router.get("/average", response_model=AveragePerformance)
async def get_average_results():
    if not DEBUG:
        raise HTTPException(status_code=503, detail="Feature not ready for live environment")

    db_handler = DatabaseHandler()
    return db_handler.calculate_average()


@router.get("/average/{start_time}/{end_time}", response_model=AveragePerformance)
async def get_average_results_by_time(start_time: str, end_time: str):
    if not DEBUG:
        raise HTTPException(status_code=503, detail="Feature not ready for live environment")

    try:
        start = datetime.fromisoformat(start_time)
        end = datetime.fromisoformat(end_time)
    except ValueError as err:
        raise HTTPException(status_code=400, detail="Invalid timestamp format. Use ISO format.") from err

    db_handler = DatabaseHandler()
    return db_handler.calculate_average(start, end)


app.include_router(router)
