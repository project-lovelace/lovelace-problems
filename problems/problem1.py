# problem1.py

import math
import random

import numpy as np

from problems.abstract_problem import AbstractProblem


class Problem1(AbstractProblem):

    def generate(self):
        v = 3.0 # [km/s]: velocity of the seismic waves

        r0 = np.array([random.uniform(-100,100), random.uniform(-100,100)])
        r1 = np.array([random.uniform(-100,100), random.uniform(-100,100)])
        r2 = np.array([random.uniform(-100,100), random.uniform(-100,100)])
        r3 = np.array([random.uniform(-100,100), random.uniform(-100,100)])

        t1 = np.linalg.norm(r1-r0) / v
        t2 = np.linalg.norm(r2-r0) / v
        t3 = np.linalg.norm(r3-r0) / v

        problem = [str(number) for number in [r1[0], r1[1], t1,
                    r2[0], r2[1], t2, r3[0], r3[1], t3]]
        solution = [str(number) for number in r0.tolist()]

        print("Input:", ' '.join(problem))
        print("Generator's solution:", ' '.join(solution))

        return problem, solution

    def solve(self, problem):
        problem = [float(number) for number in problem]

        x1 = problem[0]
        y1 = problem[1]
        t1 = problem[2]
        x2 = problem[3]
        y2 = problem[4]
        t2 = problem[5]
        x3 = problem[6]
        y3 = problem[7]
        t3 = problem[8]

        v = 3.0 # [km/s]

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
        print("Solver's solution:", solution)

        return solution

    def verify(self, answer, solution):
        x1, y1 = [float(num_str) for num_str in answer]
        x2, y2 = [float(num_str) for num_str in solution]

        error_margin = 0.0001
        error_distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)

        return error_distance < error_margin

    def test(self):
        problem, solution = self.generate()

        actual = solution
        proposed = self.solve(problem)

        is_correct = self.verify(proposed, actual)
        print("Problem solved!") if is_correct else print("Incorrect solution.")


if __name__ == '__main__':
    Problem1().test()
