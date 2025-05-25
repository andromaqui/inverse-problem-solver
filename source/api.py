from fastapi import APIRouter
from pydantic import BaseModel
import numpy as np
from solver import solve_parameters

router = APIRouter()

class FitRequest(BaseModel):
    model_type: str
    x: list[float]
    y: list[float]

@router.post("/fit")
def fit_model(data: FitRequest):
    x = np.array(data.x)
    y = np.array(data.y)
    params = solve_parameters(data.model_type, x, y)
    return {"params": params.tolist()}
