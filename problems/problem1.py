# problem1.py

import abc
import math
import random

import numpy as np

from .abstract_problem import AbstractProblem


class Problem1(AbstractProblem):

    def generate(self):
        vP = 6 # km/s
        vS = 3 # km/s

        r0 = np.array([79.0674612756, -27.0524778103])  # temporary

        # r0 = np.array([random.uniform(-100,100), random.uniform(-100,100)])
        r1 = np.array([random.uniform(-100,100), random.uniform(-100,100)])
        r2 = np.array([random.uniform(-100,100), random.uniform(-100,100)])
        r3 = np.array([random.uniform(-100,100), random.uniform(-100,100)])

        tP1 = np.linalg.norm(r1-r0) / vP
        tP2 = np.linalg.norm(r2-r0) / vP
        tP3 = np.linalg.norm(r3-r0) / vP

        tS1 = np.linalg.norm(r1-r0) / vS
        tS2 = np.linalg.norm(r2-r0) / vS
        tS3 = np.linalg.norm(r3-r0) / vS

        problem = [str(number) for number in [r1[0], r1[1], (tS1-tP1),
                     r2[0], r2[1], (tS2-tP2), r3[0], r3[1], (tS3-tP3)]]
        solution = [str(number) for number in r0.tolist()]

        print("Input:", ' '.join(problem))
        print("Generator's solution:", ' '.join(solution))

        return problem, solution


    def solve(self, problem):
        x1 = problem[0]
        y1 = problem[1]
        x2 = problem[3]
        y2 = problem[4]
        x3 = problem[6]
        y3 = problem[7]

        r0 = np.array([79.0674612756, -27.0524778103])  # temporary

        r1 = np.array([x1, y1])
        r2 = np.array([x2, y2])
        r3 = np.array([x3, y3])

        # FIXME: should not rely on solution being available!
        r1 = np.linalg.norm(r1-r0)
        r2 = np.linalg.norm(r2-r0)
        r3 = np.linalg.norm(r3-r0)

        x = ( (r1**2 - r2**2 - x1**2 + x2**2 - y1**2 + y2**2)*(y1-y3) - (r3**2 - r1**2 + x1**2 - x3**2 + y1**2 - y3**2)*(y2-y1) ) / ( 2*(x1-x3)*(y1-y2) - 2*(x1-x2)*(y1-y3) )
        y = ( x1*r2**2 - x1*r3**2 - x2*r1**2 + x2*r3**2 + x2*x1**2 - x1*x2**2 + x3*r1**2 - x3*r2**2 - x3*x1**2 + x3*x2**2 + x1*x3**2 - x2*x3**2 + x2*y1**2 - x3*y1**2 - x1*y2**2 + x3*y2**2 + x1*y3**2 - x2*y3**2) / (2 * (x2*y1 - x3*y1 - x1*y2 + x3*y2 + x1*y3 - x2*y3))

        solution = [str for number in [x, y]]

        print("Solver's solution:", solution)

        return solution

    def verify(self, answer, solution):
        x1, y1 = [float(num_str) for num_str in answer]
        x2, y2 = [float(num_str) for num_str in solution]

        error_margin = 0.0001
        error_distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)

        return error_distance < error_margin
