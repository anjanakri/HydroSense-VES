from fastapi import APIRouter
from models.schemas import VESReading, VESBulkInput, VESResult, VESBulkResult
from core.computation import compute_ves, compute_ves_bulk
from core.classification import classify_curve
import pandas as pd
import numpy as np

router=APIRouter(
    prefix="ves",
    tags=["VES Computation"]
)