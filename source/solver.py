from scipy.optimize import curve_fit
from models import linear_model, exponential_model, polynomial_model, logistic_model, sigmoid_model, powerlaw_model

def solve_parameters(model_type, x, y, p0=None):
    if model_type == "linear":
        model_func = linear_model
    elif model_type == "exponential":
        model_func = exponential_model
    elif model_type == "polynomial":
        model_func = polynomial_model
    elif model_type == "logistic":
        model_func = logistic_model
    elif model_type == "sigmoid":
        model_func = sigmoid_model
    elif model_type == "powerlaw":
        model_func = powerlaw_model
    else:
        raise ValueError(f"Unsupported model type: {model_type}")

    popt, _ = curve_fit(model_func, x, y, p0=p0)
    return popt
