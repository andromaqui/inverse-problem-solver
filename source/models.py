import numpy as np

def linear_model(x, a, b):
    return a * x + b

def exponential_model(x, a, b):
    return a * np.exp(-b * x)