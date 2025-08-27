import math

def def_e(x):
    h = 1e-5
    derivative = (math.exp(x + h) - math.exp(x - h)) / (2 * h)
    return round(derivative, 3)
