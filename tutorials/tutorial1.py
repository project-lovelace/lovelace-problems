# tutorial1.py

import logging
import math
import random

from tutorials.abstract_tutorial import AbstractTutorial

log = logging.getLogger(__name__)


class Tutorial1(AbstractTutorial):

    def generate(self):
        K   = random.randint(500, 2500)     # [geese]
        P_0 = random.randint(5, 250)        # [geese]
        r   = random.uniform(0.005, 0.025)  # [1/day]

        problem = {"K": K, "P_0": P_0, "r": r}

        log.debug("Generated problem: ", ' '.join(problem))
        log.debug("Generator cannot provide a solution.")

        return problem, None

    def solve(self, problem):
        K   = problem['K']    # [geese]
        r   = problem['r']    # [geese]
        P_0 = problem['P_0']  # [1/day]

        P = P_0
        t = 0           # [days]
        Delta_t = 0.01  # [days]

        while P < (K/2):
            P = P + (1 - P/K)*r*P*Delta_t
            t = t + Delta_t

        solution = {'t': math.floor(t)}
        print("Solver's solution: ", solution)

        return solution

    def verify(self, answer, solution):
        return answer['t'] == solution['t']
