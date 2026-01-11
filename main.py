import numpy as np
import matplotlib.pyplot as plt

from spiro import Premade
from spiro.EvaluationNode import EvaluationNode
from spiro.EvaluationRecord import EvaluationRecord
from spiro.FourierTools import fourier_analyze, fourier_extend, fourier_cut, fourier_approximate
from spiro.Functions import compound
from spiro.PlotTools import save_dialog
from spiro.Spiro import Spiro

N = 1000000
DPI = 500

if __name__ == "__main__":

    fourier_analyze(Premade.wobbly_halo, 1000000, title='Wobbly Halo')
    #fourier_analyze(Premade._wobbly_halo_arm_1, 10000, title='Rotation Arm')

    spiro = Spiro(plot_sources={
        'Wings': Premade.wings,
        #'Wings Approx': lambda n: fourier_approximate(Premade.wings, 500000, n, log_rel_tol=0.3)
    })

    figures = spiro.plot(N, save_option=False)
    plt.show()
