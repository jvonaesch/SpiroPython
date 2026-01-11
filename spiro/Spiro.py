import logging
from datetime import datetime
from typing import Iterable

import matplotlib.pyplot as plt
import numpy as np
from fontTools.ufoLib.utils import deprecated

from spiro.EvaluationNode import EvaluationNode
from spiro.EvaluationRecord import EvaluationRecord
from spiro.PlotTools import save_dialog
from spiro.Premade import wobbly_halo

LOG_PATH = 'out/logs'

class Spiro:

    def __init__(self, plot_sources, plot_size=(8, 8)):
        f_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        logging.basicConfig(filename=f'{LOG_PATH}/{f_time}.log', level=logging.INFO)
        logging.debug("initialized logger")

        self.plot_size = plot_size
        self.plot_sources = plot_sources

    def plot(self, n=100000, legend=False, save_option=False, show_title=True):
        logging.info(f"plotting with n={n}")
        
        x = np.linspace(0, 1, n)
        own_record = EvaluationRecord(x)
        figures = []
        graphs = []
        for name, source in self.plot_sources.items():
            if isinstance(source, EvaluationNode):
                graphs.append(source(own_record))
            elif isinstance(source, Iterable):
                graphs.append(source)
            else:
                graphs.append(source(n))

            fig, ax = plt.subplots()
            ax.plot(np.real(graphs[-1]), np.imag(graphs[-1]))

            fig.set_size_inches(*self.plot_size)
            if legend:
                fig.legend(name)
            if show_title:
                ax.set_title(name)
            if save_option:
                plt.show()
                save_dialog(fig, name=name)
            else:
                fig.show()
            figures.append(fig)
        return figures
