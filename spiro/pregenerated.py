import numpy as np

from spiro.Actors import compound, lambda_osc, arms, oscillator
from spiro.Evaluator import Evaluator


def wobbly_halo():
    f = Evaluator(compound, (
        lambda_osc(0.8, 1, 0.3),
        lambda_osc(0.4, 150),
        lambda_osc(0.05j, -308)
    ), name='big_comp_oscillator')
    g = Evaluator(compound, (
        lambda_osc(0.6, 1),
        lambda_osc(0.3, 153),
    ), name='small_comp_oscillator')
    h = Evaluator(arms, (f, g, 1.0, 1.1), name='wobbly_halo')
    return [h]

def double_ring():
    f = Evaluator(compound, (
        lambda_osc(0.7, 1, 0.32),
        lambda_osc(0.3, 100),
        lambda_osc(0.05j, -200)
    ), name='big_comp_oscillator')
    g = Evaluator(compound, (
        lambda_osc(0.7, -1),
        lambda_osc(0.3, -100),
    ), name='small_comp_oscillator')
    h = Evaluator(arms, (f, g, 2.0, 2.0), name='double_ring')
    return [h]

def skewed_halo():
    o1 = Evaluator(oscillator, (
        lambda x: x**1.4, 1.5, 1, 0.2
    ), name='nonlinear_osc_1')
    f = Evaluator(compound, (
        o1,
        lambda_osc(0.5, 150),
        lambda_osc(0.05j, -300)
    ), name='big_comp_oscillator')
    g = Evaluator(compound, (
        lambda_osc(2, 1),
        lambda_osc(0.4, 155),
    ), name='small_comp_oscillator')
    #osc = Evaluator(oscillator, ('t', 3, 1))
    h = Evaluator(arms, (f, g, 1.5, 1.5), name='skewed_halo')
    return [h]

def test_generator():
    f = Evaluator(compound, (
        lambda_osc(0.7, 1, 0.32),
        lambda_osc(0.3, 100),
        lambda_osc(0.05j, -200)
    ), name='big_comp_oscillator')
    g = Evaluator(compound, (
        lambda_osc(0.7, -1),
        lambda_osc(0.3, -100),
    ), name='small_comp_oscillator')
    h = Evaluator(arms, (f, g, 2.0, 2.0), name='test_gen')
    return [h]
