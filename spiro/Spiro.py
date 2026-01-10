import logging
from datetime import datetime

import matplotlib.pyplot as plt
import numpy as np

from spiro.EvaluationRecord import EvaluationRecord
from spiro.pregenerated import wobbly_halo

LOG_PATH = 'out/logs'

class Spiro:

    def __init__(self, pre_gen=wobbly_halo, plot_size=(8, 8)):
        f_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        logging.basicConfig(filename=f'{LOG_PATH}/{f_time}.log', level=logging.INFO)

        self.plot_size = plot_size
        self.evaluators = pre_gen()

    def generate_graph(self, n):
        logging.info(f'generating graph with n={n}')

        x = np.linspace(0, 1, n)
        record = EvaluationRecord(x)

        vectors = np.array([eval(record) for eval in self.evaluators])
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