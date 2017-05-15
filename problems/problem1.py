# problem1.py
# Finding earthquake epicenters

import logging
import math
import random
import numpy as np

from enum import Enum  # , auto
from abstract_problem import AbstractProblem

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('[%(asctime)s] %(name)s:%(levelname)s: %(message)s')

# create console handler
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.addHandler(ch)


class TestCase1Type(Enum):
    # TODO: Somehow include the test case descriptions within the Enum?
    GENERAL = 1
    ZERO_CASE = 2
    # ALL_CLOSE = auto()
    # ONE_FAR = auto()
    # TWO_FAR = auto()
    # ALL_FAR = auto()
    EQUIDISTANT = 3


class TestCase1:
    constants = {
        'v': 3.0  # [km/s]
    }

    testing = {
        'error_tol': 0.0001  # [km]
    }

    repeats = {
        TestCase1Type.GENERAL: 3,
        TestCase1Type.ZERO_CASE: 1,
        # TestCase1Type.ALL_CLOSE: 1,
        # TestCase1Type.ONE_FAR: 1,
        # TestCase1Type.TWO_FAR: 1,
        # TestCase1Type.ALL_FAR: 1,
        TestCase1Type.EQUIDISTANT: 1
    }

    def __init__(self, test_type):
        self.test_type = test_type
        self.user_description = ''
        self.debug_description = ''
        self.input = {}
        self.output = {}

# TODO: Is this the best way of describing the expected input/output?
# There must be a data structure that will do this for us more nicely than a dict with a commented convention?
# Inputs:
#   x1, y1, t1, x2, y2, t2, x3, y3, t3
#
# Outputs:
#   x, y: coordinates of earthquake epicenter


class Problem1(AbstractProblem):

    def __init__(self):
        self.test_cases = self.generate_test_cases()

    def generate_test_cases(self):
        logger.info("Generating test cases...")

        test_cases = []
        num_cases = sum(TestCase1.repeats.values())

        n = 1
        for test_type in TestCase1Type:
            for i in range(TestCase1.repeats[test_type]):
                logger.debug("Generating test case %d/%d...", n, num_cases)
                test_cases.append(self.generate_input(test_type))
                n = n+1

        return test_cases

    def generate_input(self, test_type):
        test_case = TestCase1(test_type)
        logger.debug("Generating test case with type %s...", test_type.name)

        # TODO: Code in check to make sure test_type is of type TestCase1Type.
        if test_type is TestCase1Type.GENERAL:
            test_case.user_description = 'General case.'

            r0 = np.array([random.uniform(-100, 100), random.uniform(-100, 100)])
            r1 = np.array([random.uniform(-100, 100), random.uniform(-100, 100)])
            r2 = np.array([random.uniform(-100, 100), random.uniform(-100, 100)])
            r3 = np.array([random.uniform(-100, 100), random.uniform(-100, 100)])
        elif test_type is TestCase1Type.ZERO_CASE:
            # TODO: Properly implement ZERO_CASE.
            test_case.user_description = 'Zero case.'
            test_case.debug_description =\
                'One of the three stations is randomly placed exactly on top of the earthquake epicenter.'

            r0 = np.array([random.uniform(-100, 100), random.uniform(-100, 100)])
            r1 = np.array([random.uniform(-100, 100), random.uniform(-100, 100)])
            r2 = r0
            r3 = np.array([random.uniform(-100, 100), random.uniform(-100, 100)])
        elif test_type is TestCase1Type.EQUIDISTANT:
            # TODO: Implement EQUIDISTANT case.
            test_case.user_description = 'Equidistant.'
            test_case.debug_description = 'All three stations are the same distance from the earthquake epicenter.'

            r0 = np.array([random.uniform(-100, 100), random.uniform(-100, 100)])
            r1 = np.array([random.uniform(-100, 100), random.uniform(-100, 100)])
            r2 = np.array([random.uniform(-100, 100), random.uniform(-100, 100)])
            r3 = np.array([random.uniform(-100, 100), random.uniform(-100, 100)])

        v = test_case.constants['v']

        t1 = np.linalg.norm(r1-r0) / v
        t2 = np.linalg.norm(r2-r0) / v
        t3 = np.linalg.norm(r3-r0) / v

        test_case.input['x1'] = r1[0]
        test_case.input['y1'] = r1[1]
        test_case.input['t1'] = t1
        test_case.input['x2'] = r2[0]
        test_case.input['y2'] = r2[1]
        test_case.input['t2'] = t2
        test_case.input['x3'] = r3[0]
        test_case.input['y3'] = r3[1]
        test_case.input['t3'] = t3

        logger.debug("Test case input:")
        logger.debug("(x1, y1, t1) = (%f, %f, %f)", r1[0], r1[1], t1)
        logger.debug("(x2, y2, t2) = (%f, %f, %f)", r2[0], r2[1], t2)
        logger.debug("(x3, y3, t3) = (%f, %f, %f)", r3[0], r3[1], t3)

        test_case.output['x'] = r0[0]
        test_case.output['y'] = r0[1]

        logger.debug("Test case solution available at creation:")
        logger.debug("(x, y) = (%f, %f)", r0[0], r0[1])

        return test_case

    def solve_test_case(self, test_case):
        v = test_case.constants['v']

        x1 = test_case.input['x1']
        y1 = test_case.input['y1']
        t1 = test_case.input['t1']
        x2 = test_case.input['x2']
        y2 = test_case.input['y2']
        t2 = test_case.input['t2']
        x3 = test_case.input['x3']
        y3 = test_case.input['y3']
        t3 = test_case.input['t3']

        # TODO: Find my derivation and write down the steps/logic here.
        # Setting up the equations, we get two simultaneous linear equations for
        # x0 and y0, namely ax + by = e and cx + dy = f where

        r1 = v*t1
        r2 = v*t2
        r3 = v*t3

        a = 2*(x2-x1)
        b = 2*(y2-y1)
        c = 2*(x3-x1)
        d = 2*(y3-y1)
        e = r1**2 - x1**2 - y1**2 - r2**2 + x2**2 + y2**2
        f = r1**2 - x1**2 - y1**2 - r3**2 + x3**2 + y3**2

        # Solving ax + by = e and cx + dy = f for x,y gives
        x = (b*f - d*e) / (b*c - a*d)
        y = (c*e - a*f) / (b*c - a*d)

        if test_case.output:  # Testing if output dict is non-empty.
            logger.warning("Test case already has solution:")
            logger.warning("(x, y) = (%f, %f)", test_case.output['x'], test_case.output['y'])
            logger.warning("Overwriting with new solution.")

        test_case.output['x'] = x
        test_case.output['y'] = y

        logger.debug("Test case solution:")
        logger.debug("(x, y) = (%f, %f)", x, y)

        return

    def test_our_solution(self):
        # Just solve the test cases we already have from initialization and verify them.
        # TODO: This should fail or throw an exception if something is wrong.
        logger.info("Testing Problem1...")
        for tc in self.test_cases:
            self.solve_test_case(tc)
            if not self.verify_user_solution(tc):
                logger.critical("Our own solution is incorrect!")
        return

    def verify_user_solution(self, test_case):
        logger.info("Verifying user solution...")

        # Extract user solution.
        user_solution = test_case.output
        user_x = user_solution['x']
        user_y = user_solution['y']

        # Recreate test case and solve it ourselves.
        tc = test_case
        tc.output = {}
        self.solve_test_case(tc)

        our_solution = tc.output
        x = our_solution['x']
        y = our_solution['y']

        # Check that solutions agree.
        error_distance = math.sqrt((x - user_x)**2 + (y - user_y)**2)  # [km]

        error_tol = test_case.testing['error_tol']

        logger.debug("User solution:")
        logger.debug("(x, y) = (%f, %f)", user_x, user_y)
        logger.debug("Our solution:")
        logger.debug("(x, y) = (%f, %f)", x, y)
        logger.debug("Error tolerance = %e. Error distance: %e.", error_tol, error_distance)

        if error_distance < error_tol:
            logger.info("User solution correct within error margin.")
            return True
        else:
            logger.info("User solution incorrect within error margin.")
            return False

if __name__ == '__main__':
    Problem1().test_our_solution()
