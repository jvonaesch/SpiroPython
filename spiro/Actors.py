import numpy as np

def osc(rad, freq, phase=0):
    return lambda x: rad * np.exp(2j * (x + phase) * freq * np.pi)

def compound(*funcs):
    return lambda x: np.sum([func(x) for func in funcs], axis=0)

def center(funcs, weights):
    weights = np.array(weights) / np.sum(weights)
    return lambda x: np.sum([f(x) * w for f, w in zip(funcs, weights)], axis=0)

def arms_numeric(a, b, rad_a, rad_b):

    a = np.asarray(a, dtype=complex)
    b = np.asarray(b, dtype=complex)
    rad_a = np.asarray(rad_a, dtype=float)
    rad_b = np.asarray(rad_b, dtype=float)

    d = np.abs(b - a)
    u = (b - a) / d

    x = (rad_a ** 2 - rad_b ** 2 + d ** 2) / (2 * d)
    mask = (rad_a ** 2 - x ** 2) < 0
    y = np.sqrt(np.abs(rad_a ** 2 - x ** 2))
    y[mask] = None

    delta1 = u * x + 1j * u * y
    delta2 = u * x - 1j * u * y

    return a + delta1


def arms(func_a, func_b, rad_a, rad_b):
    return lambda x: arms_numeric(func_a(x), func_b(x), rad_a, rad_b)
