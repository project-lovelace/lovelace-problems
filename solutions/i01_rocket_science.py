import math

v_e = 2550  # [m/s]
M = 250000  # [kg]


def solution(v):
    return M * (math.exp(v / v_e) - 1)
