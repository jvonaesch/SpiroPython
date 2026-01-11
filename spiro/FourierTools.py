import numpy as np
import matplotlib.pyplot as plt


def fourier_analyze(f, n=1000):
    x = np.linspace(0, 1, n)
    y = f(x)
    c = np.fft.fft(y)
    c = np.fft.fftshift(c)

    fig, axs = plt.subplots(nrows=2)
    axs[0].semilogy(np.arange(-n+n//2, n//2), np.abs(c))
    axs[1].plot(np.arange(-n+n//2, n//2), np.angle(c))
    fig.legend("c")
    fig.show()

def fourier_cut(f, n=1000, rel_tol=0, abs_tol=0, log_tol=0):
    x = np.linspace(0, 1, n)
    y = f(x)
    c = np.fft.fft(y)

    c_cut = c.copy()
    c_cut[np.abs(c) < (rel_tol * np.max(np.abs(c)))] = 0
    c_cut[np.abs(c) < abs_tol] = 0
    c_cut[np.log(np.abs(c)) <= (log_tol * np.log(np.max(np.abs(c))))] = 0
    return c_cut

def fourier_extend(c, n):
    old_n = len(c)
    m = np.min((old_n, n))

    c_ext = np.zeros(n, dtype=complex)
    c_ext[:m//2] = c[:m//2]
    c_ext[-m+m//2:] = c[-m+m//2:]

    x = np.fft.ifft(c_ext) * (n / old_n)
    return x
