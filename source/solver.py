from scipy.optimize import curve_fit
from source.models import linear_model, exponential_model

def solve_parameters(model_type, x, y, p0=None):
    if model_type == "linear":
        model_func = linear_model
    elif model_type == "exponential":
        model_func = exponential_model
    else:
        raise ValueError(f"Unsupported model type: {model_type}")

    popt, _ = curve_fit(model_func, x, y, p0=p0)
    return popt
