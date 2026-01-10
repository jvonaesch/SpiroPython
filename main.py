import numpy as np
import matplotlib.pyplot as plt

from spiro.PlotTools import save_dialog
from spiro.Spiro import Spiro
from spiro.pregenerated import wobbly_halo, test_generator

N = 1000000
DPI = 500

if __name__ == "__main__":

    spiro = Spiro(pre_gen=test_generator)
    figure = spiro.plot(N)
    plt.show()
    save_dialog(figure)
