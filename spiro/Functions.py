import numpy as np

def oscillator(t, rad, freq, phase=0):
    return rad * np.exp(2j * (t + phase) * freq * np.pi)

def compound(*vectors):
    return np.sum(vectors, axis=0)

def arms(a, b, rad_a, rad_b, patch_disconnects=False):
    a = np.asarray(a, dtype=complex)
    b = np.asarray(b, dtype=complex)
    rad_a = np.asarray(rad_a, dtype=float)
    rad_b = np.asarray(rad_b, dtype=float)

    d = np.abs(b - a)
    u = (b - a) / d

    x = (rad_a ** 2 - rad_b ** 2 + d ** 2) / (2 * d)

    if patch_disconnects:
        inner = rad_a ** 2 - x ** 2
        y = np.sign(inner) * np.sqrt(np.abs(inner))
    else:
        mask = (rad_a ** 2 - x ** 2) < 0
        y = np.sqrt(np.abs(rad_a ** 2 - x ** 2))
        y[mask] = None

    delta1 = u * x + 1j * u * y
    delta2 = u * x - 1j * u * y

    return a + delta1

def lambda_center(funcs, weights):
    weights = np.array(weights) / np.sum(weights)
    return lambda x: np.sum([f(x) * w for f, w in zip(funcs, weights)], axis=0)

def lambda_osc(rad, freq, phase=0):
    return lambda x: rad * np.exp(2j * (x + phase) * freq * np.pi)

def lambda_compound(*funcs):
    return lambda x: compound(*[func(x) for func in funcs])

def lambda_arms(func_a, func_b, rad_a, rad_b):
    return lambda x: arms(func_a(x), func_b(x), rad_a, rad_b)
