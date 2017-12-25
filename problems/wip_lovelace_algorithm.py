# problem5.py
# Lovelace's algorithm
# Haven't decided what we're testing yet.

import random

import numpy as np
from problems.abstract_problem import AbstractProblem


class Problem5(AbstractProblem):
    def generate(self):
        return random.randint(3, 500)

    @staticmethod
    def bernoulli_lovelace(n, B=None):
        from fractions import Fraction
        if B is None:
            B = {}

        if n in B.keys():
            return B[n]
        elif (n < 1) or (np.mod(n, 2) == 0):
            return 0
        else:
            # My calculations gave me a formula for B_{2n+1} so I am actually
            # calculating B_{2m+1} = B_n where m = (n+1)/2.
            m = int((n+1)/2)
            Bn = Fraction(2*m-1, 4*m+2)
            for i in range(1, 2*m-3 + 1):
                numerator = 1
                for j in range(2*m-(i-1), 2*m + 1):
                    numerator *= j

                denominator = 1
                for j in range(2, i+1 + 1):
                    denominator *= j

                Bi = Problem5.bernoulli_lovelace(i, B)
                Bn = Bn - Fraction(numerator, denominator)*Bi

            B[n] = Bn  # Store the nth Bernoulli number in the dictionary.
            return Bn

    def solve(self, problem):
        return self.bernoulli_lovelace(problem)

    def verify(self, proposed, actual):
        return proposed == actual

    def test(self):
        problem = self.generate()
        print(problem)

        solution = self.solve(problem)
        print(solution)

if __name__ == '__main__':
    import time

    # Testing run time when creating a new dictionary B each call.
    start = time.clock()
    for i in range(1, 151):
        Problem5().bernoulli_lovelace(i)
        # print('{:03d}  '.format(i) + str(Problem5().bernoulli_lovelace(i)))
    end = time.clock()
    print(end - start)

    # Testing run time with the dictionary being shared between calls.
    start = time.clock()
    B = {}
    for i in range(1, 151):
        Problem5().bernoulli_lovelace(i, B)
        # print('{:03d}  '.format(i) + str(Problem5().bernoulli_lovelace(i, B)))
    end = time.clock()
    print(end - start)
