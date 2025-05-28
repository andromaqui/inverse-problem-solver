from models import linear_model, exponential_model, polynomial_model, logistic_model, sigmoid_model, powerlaw_model
from scipy.optimize import minimize
from regularizationtype import RegularizationType

def solve_parameters(model_type, x, y, p0=None, regularization: str = None, alpha: float = 0.1):
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

    reg = calculate_reg_type(regularization)
    popt = solve_parameters_regularized(model_func, x, y, p0, alpha=alpha, reg_type=reg)
    return popt

def solve_parameters_regularized(model_func, x, y, p0, alpha, reg_type=RegularizationType.NONE):
    def loss(params):
        residual = y - model_func(x, *params)
        if reg_type == RegularizationType.L2:
            penalty = alpha * sum(p**2 for p in params)
        elif reg_type == RegularizationType.L1:
            penalty = alpha * sum(abs(p) for p in params)
        elif reg_type == RegularizationType.TV:
            penalty = alpha * sum(abs(params[i + 1] - params[i]) for i in range(len(params) - 1))
        elif reg_type == RegularizationType.TGV:
            second_diff = [params[i + 2] - 2 * params[i + 1] + params[i] for i in range(len(params) - 2)]
            penalty = alpha * sum(abs(d) for d in second_diff)
        else:
            penalty = 0
        return sum(residual**2) + penalty

    print(f"a {alpha}")
    result = minimize(loss, p0)
    return result.x

def calculate_reg_type(regularization: str = None):
    if (regularization == "L1"):
        return  RegularizationType.L1
    elif (regularization == "L2"):
        return RegularizationType.L2
    elif (regularization == "TV"):
        return RegularizationType.TV
    elif (regularization == "TGV"):
        return RegularizationType.TGV
    else:
        return RegularizationType.NONE
