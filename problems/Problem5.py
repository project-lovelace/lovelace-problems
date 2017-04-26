# problem5.py
# Lovelace's algorithm

import random
import numpy as np

from problems.abstract_problem import AbstractProblem


class Problem5(AbstractProblem):
    def generate(self):
        return {'n': random.randint(3, 10)}

    @staticmethod
    def bernoulli_lovelace(n, B=None):
        from fractions import Fraction
        if B == None:
            B = {}

        if (n < 1) or (np.mod(n, 2) == 0):
            return 0
        elif n in B.keys():
            return B[n]
        else:
            m = int((n+1)/2)
            Bn = Fraction(2*m-1, 4*m+2)
            for i in range(1, 2*m-3 + 1):
                numerator = 1
                for j in range(2*m-(i-1), 2*m + 1):
                    numerator *= j

                denominator = 1
                for j in range(2, i+1 + 1):
                    denominator *= j

                #print(Bn)
                #print(numerator, denominator)
                #print(Problem5.bernoulli_lovelace(i, B))
                Bn = Bn - Fraction(numerator, denominator) * Problem5.bernoulli_lovelace(i, B)

            B[n] = Bn
            return Bn

    def solve(self, problem):
        return

    def verify(self, proposed, actual):
        return proposed == actual

    def test(self):
        problem = self.generate()
        print(problem)

        solution = self.solve(problem)
        print(solution)

if __name__ == '__main__':
    import time

    start = time.clock()
    for i in range(1, 151):
        Problem5().bernoulli_lovelace(i)
        # print('{:03d}  '.format(i) + str(Problem5().bernoulli_lovelace(i)))
    end = time.clock()
    print(end - start)

    start = time.clock()
    B = {}
    for i in range(1, 151):
        Problem5().bernoulli_lovelace(i, B)
        # print('{:03d}  '.format(i) + str(Problem5().bernoulli_lovelace(i, B)))
    end = time.clock()
    print(end - start)