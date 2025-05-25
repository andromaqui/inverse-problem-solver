from models import (linear_model, exponential_model,
                    powerlaw_model, sigmoid_model, logistic_model, polynomial_model)

def evaluate_model(model_type, x, params):
    if model_type == "linear":
        return linear_model(x, **params)
    elif model_type == "exponential":
        return exponential_model(x, **params)
    elif model_type == "polynomial":
        return polynomial_model(x, **params)
    elif model_type == "logistic":
        return logistic_model(x, **params)
    elif model_type == "sigmoid":
        return sigmoid_model(x, **params)
    elif model_type == "powerlaw":
        return powerlaw_model(x, **params)
    else:
        raise ValueError(f"Unsupported model type: {model_type}")
