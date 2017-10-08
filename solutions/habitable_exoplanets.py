import numpy as np

input_str = str(input())
input_list = input_str.split()
problem = [float(number) for number in input_list]

L_star = problem[0]
r = problem[1]

if r < np.sqrt(L_star/1.1):
    print('too hot')
elif r > np.sqrt(L_star/0.53):
    print('too cold')
else:
    print('just right')