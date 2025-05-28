from fastapi import APIRouter, FastAPI, UploadFile, File
from pydantic import BaseModel
import numpy as np
from solver import solve_parameters
from scipy.signal import wiener
from PIL import Image
import io
from starlette.responses import StreamingResponse

router = APIRouter()

class FitRequest(BaseModel):
    model_type: str
    x: list[float]
    y: list[float]
    regularization: str
    alpha: float

@router.post("/fit")
def fit_model(data: FitRequest):
    x = np.array(data.x)
    y = np.array(data.y)
    y0 = guess_p0(data.model_type, x, y)
    params = solve_parameters(data.model_type, x, y, y0, data.regularization, data.alpha)
    return {"params": params.tolist()}

@router.post("/deblur")
async def deblur_image(file: UploadFile = File(...)):
    img = Image.open(file.file).convert("L")
    img_np = np.array(img)

    deblurred_np = wiener(img_np, (5, 5))
    deblurred_img = Image.fromarray(np.uint8(np.clip(deblurred_np, 0, 255)))

    buf = io.BytesIO()
    deblurred_img.save(buf, format="PNG")
    buf.seek(0)

    return StreamingResponse(buf, media_type="image/png")

def guess_p0(model_type, x, y):
    if model_type == "linear":
        a = (y[-1] - y[0]) / (x[-1] - x[0]) if x[-1] != x[0] else 1.0
        b = y[0] - a * x[0]
        return [a, b]

    elif model_type == "exponential":
        return [y[0] if y[0] > 0 else 1.0, 0.1]

    elif model_type == "polynomial":
        return [1.0, 0.0, 0.0]

    elif model_type == "logistic":
        L = max(y)
        x0 = x[np.argmax(np.gradient(y))]
        return [L, 1.0, x0]

    elif model_type == "sigmoid":
        b = x[np.argmax(np.gradient(y))]
        a = 1.0
        return [a, b]

    elif model_type == "powerlaw":
        return [1.0, 1.0]

    else:
        raise ValueError(f"No p0 guess implemented for model: {model_type}")
