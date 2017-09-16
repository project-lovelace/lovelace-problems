import sys

input_str = str(input())
input_list = input_str.split()
problem = [float(number) for number in input_list]

x1 = problem[0]
y1 = problem[1]
t1 = problem[2]
x2 = problem[3]
y2 = problem[4]
t2 = problem[5]
x3 = problem[6]
y3 = problem[7]
t3 = problem[8]

v = 3.0  # [km/s]

r1 = v*t1
r2 = v*t2
r3 = v*t3

# TODO: Find my derivation and write down the steps/logic here.
# Setting up the equations, we get two simultaneous linear equations for
# x0 and y0, namely ax + by = e and cx + dy = f where

a = 2*(x2-x1)
b = 2*(y2-y1)
c = 2*(x3-x1)
d = 2*(y3-y1)
e = r1**2 - x1**2 - y1**2 - r2**2 + x2**2 + y2**2
f = r1**2 - x1**2 - y1**2 - r3**2 + x3**2 + y3**2

# Solving ax + by = e and cx + dy = f for x,y gives
x = (b*f - d*e) / (b*c - a*d)
y = (c*e - a*f) / (b*c - a*d)

solution = [str(number) for number in [x, y]]
print(solution[0], solution[1])
