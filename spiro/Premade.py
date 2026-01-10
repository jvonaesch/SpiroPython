import numpy as np

from spiro.Functions import compound, lambda_osc, arms, oscillator
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

def seven_blob():
    base_1 = 1
    base_2 = 600
    offset = 7
    g = Evaluator(compound, (
        lambda_osc(2.1, base_1, phase=0.5),
        lambda_osc(0.9, base_1 + offset, phase=0.25),
        lambda_osc(0.2, base_2),
        lambda_osc(0.5, base_2 + offset)
    ), name='seven_blob')
    return [g]

def five_wobble():
    base_1 = 1
    base_2 = 500
    offset = 5
    f = Evaluator(compound, (
        lambda_osc(2.5, base_1),
        lambda_osc(0.7, base_1 + offset),
        lambda_osc(0.2j, base_2),
        lambda_osc(0.5, base_2 + offset * 3)
    ), name='five_wobble')
    g = Evaluator(arms, (
        lambda_osc(0.5j, -1),
        f, 2, 2), name='blobble')
    return [f]

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

