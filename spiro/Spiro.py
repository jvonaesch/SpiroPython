import logging
from datetime import datetime

import matplotlib.pyplot as plt
import numpy as np

from spiro.Actors import lambda_osc, lambda_arms, lambda_compound, compound, arms
from spiro.EvaluationRecord import EvaluationRecord
from spiro.Evaluator import Evaluator
from spiro.FourierTools import fourier_analyze

LOG_PATH = 'out/logs'

def construct_evaluators():
    F = Evaluator(compound, (
        lambda_osc(0.8, 1, 0.3),
        lambda_osc(0.4, 150),
        lambda_osc(0.05j, -308)
    ), name='big_comp_oscillator')
    G = Evaluator(compound, (
        lambda_osc(0.6, 1),
        lambda_osc(0.3, 153),
    ), name='small_comp_oscillator')
    H = Evaluator(arms, (F, G, 1.0, 1.1), name='arms_oscillator')

    return [G, H]

    #fourier_analyze(h, 10000)
    #return [h]

class Spiro:

    def __init__(self, plot_size=(8, 8)):
        f_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        logging.basicConfig(filename=f'{LOG_PATH}/{f_time}.log', level=logging.INFO)

        self.plot_size = plot_size
        self.evaluators = construct_evaluators()

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