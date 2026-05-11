from fastapi import APIRouter
from models.schemas import VESReading, VESBulkInput, VESResult, VESManyResult
from core.computation import compute_ves, compute_ves_bulk, K_factor
from core.classification import classify_curve, classify_water_quality
import pandas as pd
import numpy as np

router=APIRouter(
    prefix="/ves",
    tags=["VES Computation"]
)

@router.post("/compute", response_model=VESResult)
def compute_signal(reading: VESReading):
    app_resistivity=compute_ves(reading.ab, reading.mn, reading.voltage, reading.current)
    K= K_factor(reading.ab, reading.mn)
    return VESResult(
        ab=reading.ab,
        mn=reading.mn,
        voltage=reading.voltage,
        current= reading.current,
        k_factor=K,
        app_resistivity=app_resistivity
    )