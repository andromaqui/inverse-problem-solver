import numpy as np

def linear_model(x, a, b):
    return a * x + b

def exponential_model(x, a, b):
    return a * np.exp(-b * x)

def polynomial_model(x, a, b, c):
    return a * x**2 + b * x + c

def logistic_model(x, L, k, x0):
    return L / (1 + np.exp(-k * (x - x0)))

def sigmoid_model(x, a, b):
    return 1 / (1 + np.exp(-a * (x - b)))

def powerlaw_model(x, a, b):
    return a * x**b
