import logging
from datetime import datetime

import matplotlib.pyplot as plt
import numpy as np

from spiro.Actors import compound, osc, arms
from spiro.FourierTools import fourier_analyze

LOG_PATH = 'out/logs'

def construct():
    f = compound(
        osc(0.8, 1, 0.3),
        osc(0.4, 150),
        osc(0.05j, -308)
    )
    g = compound(
        osc(0.6, 1),
        osc(0.3, 153),
    )
    h = arms(f, g, 1.0, 1.1)
    #fourier_analyze(h, 10000)

    return [h]

class Spiro:

    def __init__(self, plot_size=(8, 8)):
        f_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        logging.basicConfig(filename=f'{LOG_PATH}/{f_time}.log', level=logging.INFO)

        self.plot_size = plot_size
        self.funcs = construct()

    def generate_graph(self, n):
        logging.info(f'generating graph with n={n}')

        x = np.linspace(0, 1, n)
        vectors = np.array([func(x) for func in self.funcs])
        return vectors

    def plot(self, n=100000):
        logging.info(f"plotting with n={n}")

        fig, ax = plt.subplots()
        lines = self.generate_graph(n)

        for line in lines:
            ax.plot(np.real(line), np.imag(line))
        fig.set_size_inches(*self.plot_size)
        fig.show()
        return fig