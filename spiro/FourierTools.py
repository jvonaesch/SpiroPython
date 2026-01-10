import numpy as np
import matplotlib.pyplot as plt


def fourier_analyze(f, n=1000):
    x = np.linspace(0, 1, n)
    y = f(x)
    c = np.fft.fft(y)
    c = np.fft.fftshift(c)

    figure, axes = plt.subplots()
    axes.semilogy(np.arange(-n+n//2, n//2), np.abs(c))
    figure.legend("c")
    figure.show()

def fourier_cut(f, n=1000, fac=0.1):
    x = np.linspace(0, 1, n)
    y = f(x)
    c = np.fft.fft(y)

    c_cut = c.copy()
    c_cut[np.abs(c) < (fac * np.max(np.abs(c)))] = 0
    return c_cut

def fourier_extend(c, n):
    old_n = len(c)
    m = np.min((old_n, n))

    c_ext = np.zeros(n, dtype=complex)
    c_ext[:m//2] = c[:m//2]
    c_ext[-m+m//2:] = c[-m+m//2:]

    x = np.fft.ifft(c_ext) * (n / old_n)
    return x
