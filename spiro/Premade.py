import numpy as np

from spiro.Functions import compound, lambda_osc, arms, oscillator
from spiro.EvaluationNode import EvaluationNode


_wobbly_halo_arm_1 = EvaluationNode(compound, (
    lambda_osc(0.8, 1, 0.3),
    lambda_osc(0.4, 150),
    lambda_osc(0.05j, -308)
), name='wobbly_halo_arm_1')
_wobbly_halo_arm_2 = EvaluationNode(compound, (
    lambda_osc(0.6, 1),
    lambda_osc(0.3, 153),
), name='wobbly_halo_arm_2')
wobbly_halo = EvaluationNode(arms, (_wobbly_halo_arm_1, _wobbly_halo_arm_2, 1.0, 1.1), name='wobbly_halo')


_double_ring_arm_1 = EvaluationNode(compound, (
    lambda_osc(0.7, 1, 0.32),
    lambda_osc(0.3, 100),
    lambda_osc(0.05j, -200)
), name='double_ring_arm_1')
_double_ring_arm_2 = EvaluationNode(compound, (
    lambda_osc(0.7, -1),
    lambda_osc(0.3, -100),
), name='double_ring_arm_2')
double_ring = EvaluationNode(arms, (_double_ring_arm_1, _double_ring_arm_2, 2.0, 2.0), name='double_ring')


_skewed_halo_nonlinear_osc = EvaluationNode(oscillator, (
    lambda x: x**1.4, 1.5, 1, 0.2
), name='skewed_halo_nonlinear_osc')
_skewed_halo_arm_1 = EvaluationNode(compound, (
    _skewed_halo_nonlinear_osc,
    lambda_osc(0.5, 150),
    lambda_osc(0.05j, -300)
), name='skewed_halo_arm_1')
_skewed_halo_arm_2 = EvaluationNode(compound, (
    lambda_osc(2, 1),
    lambda_osc(0.4, 155),
), name='skewed_halo_arm_2')
skewed_halo = EvaluationNode(arms, (_skewed_halo_arm_1, _skewed_halo_arm_2, 1.5, 1.5), name='skewed_halo')

def multi_blob(base_rot=600, offset=7):
    f = EvaluationNode(compound, (
        lambda_osc(2.1, 1, phase=0.5),
        lambda_osc(0.9, 1 + offset, phase=0.25),
        lambda_osc(0.2, base_rot),
        lambda_osc(0.5, base_rot + offset)
    ), name=f'{offset}_blob_{base_rot}')
    return f


def multi_wobble(base_rot=500, offset=5):
    f = EvaluationNode(compound, (
        lambda_osc(2.5, 1),
        lambda_osc(0.7, 1 + offset),
        lambda_osc(0.2j, base_rot),
        lambda_osc(0.5, base_rot + offset * 3)
    ), name=f'{offset}_wobble_{base_rot}')
    return f


_wings_osc_0 = EvaluationNode(compound, (
    lambda_osc(0.7, 1, 0.32),
    lambda_osc(0.3, 100),
    lambda_osc(0.05j, -200)
), name='_wings_osc_0')
_wings_osc_1 = EvaluationNode(compound, (
    lambda_osc(0.7, -1),
    lambda_osc(0.3, -100),
), name='_wings_osc_1')
_wings_arms_0 = EvaluationNode(arms, (_wings_osc_0, _wings_osc_1, 2.0, 2.0), name='_wings_arms_0')
_wings_base_0 = EvaluationNode(compound, (_wings_arms_0, lambda_osc(4, 1)), name='_wings_base_0')
_wings_base_1 = EvaluationNode(compound, (
    lambda_osc(0.2, 200),
    lambda_osc(6, 1, 0.2)
), name='_wings_base_1')
wings = EvaluationNode(arms, (_wings_base_0, _wings_base_1, 7.0, 7.0), name='wings')

