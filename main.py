import numpy as np
import matplotlib.pyplot as plt

from spiro.PlotTools import save_dialog
from spiro.Spiro import construct_evaluators, Spiro

N = 1000000
DPI = 500

if __name__ == "__main__":

    spiro = Spiro()
    figure = spiro.plot(N)
    plt.show()
    # save_dialog(figure)