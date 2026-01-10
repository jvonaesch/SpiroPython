
from Spiro import compound, lambda_osc

base_1 = 1
base_2 = 400
offset = 7
g = compound(
    lambda_osc(1.8, base_1, phase=0.5),
    lambda_osc(0.9, base_1 + offset, phase=0.25),
    lambda_osc(0.2, base_2),
    lambda_osc(0.5, base_2 + offset)
)

base_1 = 1
base_2 = 500
offset = 5
f = compound(
    lambda_osc(2.5, base_1),
    lambda_osc(1, base_1 + offset),
    lambda_osc(0.2j, base_2),
    lambda_osc(0.5, base_2 + offset * 3)
)
