
from Spiro import compound, osc

base_1 = 1
base_2 = 400
offset = 7
g = compound(
    osc(1.8, base_1, phase=0.5),
    osc(0.9, base_1 + offset, phase=0.25),
    osc(0.2, base_2),
    osc(0.5, base_2 + offset)
)

base_1 = 1
base_2 = 500
offset = 5
f = compound(
    osc(2.5, base_1),
    osc(1, base_1 + offset),
    osc(0.2j, base_2),
    osc(0.5, base_2 + offset*3)
)
