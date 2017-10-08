import numpy as np

input_str = str(input())
input_list = input_str.split()
problem = [float(number) for number in input_list]

v = problem[0]

# TODO: get actual values.
v_e = 250  # [m/s]
M = 12000  # [kg]

print(M*(np.exp(v/v_e) - 1))