from models import linear_model, exponential_model

def evaluate_model(model_type, x, params):
    if model_type == "linear":
        return linear_model(x, **params)
    elif model_type == "exponential":
        return exponential_model(x, **params)
    else:
        raise ValueError(f"Unsupported model type: {model_type}")
