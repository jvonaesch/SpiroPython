import numpy as np
import matplotlib.pyplot as plt

from spiro import Premade
from spiro.EvaluationNode import EvaluationNode
from spiro.EvaluationRecord import EvaluationRecord
from spiro.FourierTools import fourier_analyze, fourier_extend, fourier_cut
from spiro.Functions import compound
from spiro.PlotTools import save_dialog
from spiro.Spiro import Spiro

N = 1000000
DPI = 500

if __name__ == "__main__":

    wings_func = lambda x: Premade.wings(EvaluationRecord(x))
    fourier_analyze(wings_func, 500000)

    spiro = Spiro(root_nodes={
        node.name: node for node in (
            #Premade._wings_base_0,
            #Premade._wings_arms_0,
            EvaluationNode(compound, [
                lambda x: fourier_extend(fourier_cut(wings_func, 500000, log_tol=0.2), len(x))
            ], name='fourier log. tol 1'),
            EvaluationNode(compound, [
                lambda x: fourier_extend(fourier_cut(wings_func, 500000, abs_tol=1), len(x))
            ], name='fourier abs. tol 1'),
            Premade.wings,
        )
    })

    figures = spiro.plot(N, save_option=False)
    plt.show()
