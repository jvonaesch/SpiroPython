import logging
from datetime import datetime

import matplotlib.pyplot as plt
import numpy as np
from fontTools.ufoLib.utils import deprecated

from spiro.EvaluationRecord import EvaluationRecord
from spiro.PlotTools import save_dialog
from spiro.Premade import wobbly_halo

LOG_PATH = 'out/logs'

class Spiro:

    def __init__(self, root_nodes, plot_size=(8, 8)):
        f_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        logging.basicConfig(filename=f'{LOG_PATH}/{f_time}.log', level=logging.INFO)
        logging.debug("initialized logger")

        self.plot_size = plot_size
        self.root_nodes = root_nodes

    def plot(self, n=100000, legend=False, save_option=False, show_title=True):
        logging.info(f"plotting with n={n}")
        
        x = np.linspace(0, 1, n)
        record = EvaluationRecord(x)
        lines = np.array([node(record) for node in self.root_nodes.values()])
        names = self.root_nodes.keys()

        figures = []
        for line, name in zip(lines, names):
            fig, ax = plt.subplots()
            ax.plot(np.real(line), np.imag(line))

            fig.set_size_inches(*self.plot_size)
            if legend:
                fig.legend(names)
            if show_title:
                ax.set_title(name)
            if save_option:
                plt.show()
                save_dialog(fig, name=name)
            else:
                fig.show()
            figures.append(fig)
        return figures
