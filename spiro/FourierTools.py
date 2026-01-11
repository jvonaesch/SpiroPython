import numpy as np
import matplotlib.pyplot as plt


def fourier_analyze(f, n=1000, title=''):
    x = np.linspace(0, 1, n)
    y = f(x)
    c = np.fft.fft(y)
    c = np.fft.fftshift(c)

    fig, axs = plt.subplots(nrows=2)
    axs[0].semilogy(np.arange(-n+n//2, n//2), np.abs(c))
    axs[0].set_title(f'absolute values and angles of fourier spectrum of {title}')
    axs[1].plot(np.arange(-n+n//2, n//2), np.angle(c))
    #axs[1].set_title(f'complex angles of fourier spectrum of {title}')
    fig.legend("c")
    fig.show()

def fourier_cut(f, n=1000, rel_tol=0, abs_tol=0, log_rel_tol=0, log_abs_tol=0):
    x = np.linspace(0, 1, n)
    y = f(x)
    c = np.fft.fft(y)

    c_cut = c.copy()
    c_cut[np.abs(c) < (rel_tol * np.max(np.abs(c)))] = 0
    c_cut[np.abs(c) < abs_tol] = 0
    c_cut[np.log(np.abs(c)) <= (log_rel_tol * np.log(np.max(np.abs(c))))] = 0
    c_cut[np.log(np.abs(c)) < log_abs_tol] = 0
    return c_cut

def fourier_extend(c, n):
    old_n = len(c)
    m = np.min((old_n, n))

    c_ext = np.zeros(n, dtype=complex)
    c_ext[:m//2] = c[:m//2]
    c_ext[-m+m//2:] = c[-m+m//2:]

    x = np.fft.ifft(c_ext) * (n / old_n)
    return x

def fourier_approximate(f, num_bases, num_evals, rel_tol=0, abs_tol=0, log_rel_tol=0, log_abs_tol=0):
    cut = fourier_cut(
        f, num_bases,
        rel_tol=rel_tol, abs_tol=abs_tol, log_rel_tol=log_rel_tol, log_abs_tol=log_abs_tol
    )
    return fourier_extend(cut, num_evals)
