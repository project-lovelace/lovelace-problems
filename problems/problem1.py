# problem1.py
# Finding earthquake epicenters

import logging
import math
import random
import numpy as np

from enum import Enum  # , auto
from problems.abstract_problem import AbstractProblem

# TODO: Store logger config in an ini-style file?
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('[%(asctime)s] %(name)s:%(levelname)s: %(message)s')

# create console handler and add it to the logger
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.addHandler(ch)


class TestCase1Type(Enum):
    GENERAL = ('General case', '', 3)
    ZERO_CASE = ('Zero case',
                 'One of the three stations is randomly placed exactly on top of the earthquake epicenter.',
                 1)
    # ALL_CLOSE = auto()
    # ONE_FAR = auto()
    # TWO_FAR = auto()
    # ALL_FAR = auto()
    EQUIDISTANT = ('Equidistant case', 'All three stations are the same distance from the earthquake epicenter.', 1)
    UNKNOWN = ('Unknown case',
               'Used when given the input of a test case but not its type. Primarily used by '
               + 'AbstractProblem.verify_user_solution.',
               0)

    def __init__(self, test_name, debug_description, multiplicity):
        self.test_name = test_name
        self.debug_description = debug_description
        self.multiplicity = multiplicity


class TestCase1:
    def __init__(self, test_type):
        self.test_type = test_type
        self.input = {}
        self.output = {}

    def input_str(self):
        input_str = str(self.input['x1']) + ' ' + str(self.input['y1']) + ' ' + str(self.input['t1']) + ' '
        input_str += str(self.input['x2']) + ' ' + str(self.input['y2']) + ' ' + str(self.input['t2']) + ' '
        input_str += str(self.input['x3']) + ' ' + str(self.input['y3']) + ' ' + str(self.input['t3'])
        return input_str

    def output_str(self):
        return str(self.output['x']) + ' ' + str(self.output['y'])

# TODO: Is this the best way of describing the expected input/output?
# There must be a data structure that will do this for us more nicely than a dict with a commented convention?
# Inputs:
#   x1, y1, t1, x2, y2, t2, x3, y3, t3
#
# Outputs:
#   x, y: coordinates of earthquake epicenter


class Problem1(AbstractProblem):
    constants = {
        'v': 3.0  # [km/s]
    }

    testing = {
        'error_tol': 0.0001  # [km]
    }

    def __init__(self):
        self.test_cases = self.generate_test_cases()

    def generate_test_cases(self):
        logger.info("Generating test cases...")
        test_cases = []

        # Count number of test cases we'll be generating in total.
        num_cases = 0
        for test_type in TestCase1Type:
            num_cases += test_type.multiplicity

        # Generate all the cases and store them in test_cases.
        n = 1
        for test_type in TestCase1Type:
            for i in range(test_type.multiplicity):
                logger.debug("Generating test case %d/%d...", n, num_cases)
                test_cases.append(self.generate_input(test_type))
                n = n+1

        return test_cases

    def generate_input(self, test_type):
        if not isinstance(test_type, TestCase1Type):
            logger.critical('test_type is not of type TestCase1Type!')
            raise TypeError('test_type is not of type TestCase1Type!')

        test_case = TestCase1(test_type)
        logger.debug("Generating %s...", test_type.test_name)

        # TODO: Code in check to make sure test_type is of type TestCase1Type.
        if test_type is TestCase1Type.GENERAL:
            r0 = np.array([random.uniform(-100, 100), random.uniform(-100, 100)])
            r1 = np.array([random.uniform(-100, 100), random.uniform(-100, 100)])
            r2 = np.array([random.uniform(-100, 100), random.uniform(-100, 100)])
            r3 = np.array([random.uniform(-100, 100), random.uniform(-100, 100)])
        elif test_type is TestCase1Type.ZERO_CASE:
            # TODO: Properly implement ZERO_CASE.
            r0 = np.array([random.uniform(-100, 100), random.uniform(-100, 100)])
            r1 = np.array([random.uniform(-100, 100), random.uniform(-100, 100)])
            r2 = r0
            r3 = np.array([random.uniform(-100, 100), random.uniform(-100, 100)])
        elif test_type is TestCase1Type.EQUIDISTANT:
            # TODO: Implement EQUIDISTANT case.
            r0 = np.array([random.uniform(-100, 100), random.uniform(-100, 100)])
            r1 = np.array([random.uniform(-100, 100), random.uniform(-100, 100)])
            r2 = np.array([random.uniform(-100, 100), random.uniform(-100, 100)])
            r3 = np.array([random.uniform(-100, 100), random.uniform(-100, 100)])
        else:
            logger.critical('test_type is not a known case type!')
            raise ValueError('test_type is not a known case type!')

        v = self.constants['v']

        t1 = np.linalg.norm(r1-r0) / v
        t2 = np.linalg.norm(r2-r0) / v
        t3 = np.linalg.norm(r3-r0) / v

        test_case.input = {'x1': r1[0], 'y1': r1[1], 't1': t1,
                           'x2': r2[0], 'y2': r2[1], 't2': t2,
                           'x3': r3[0], 'y3': r3[1], 't3': t3}

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
        v = self.constants['v']

        x1, y1, t1 = test_case.input['x1'], test_case.input['y1'], test_case.input['t1']
        x2, y2, t2 = test_case.input['x2'], test_case.input['y2'], test_case.input['t2']
        x3, y3, t3 = test_case.input['x3'], test_case.input['y3'], test_case.input['t3']

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
            if not self.verify_user_solution(tc.input_str(), tc.output_str()):
                logger.critical("Our own solution is incorrect!")
        return

    def verify_user_solution(self, user_input_str, user_output_str):
        logger.info("Verifying user solution...")
        logger.debug("User input string: %s", user_input_str)
        logger.debug("User output string: %s", user_output_str)

        # Build TestCase object out of user's input string.
        tmp_test_case = TestCase1(TestCase1Type.UNKNOWN)

        inputs = list(map(float, user_input_str.split()))
        x1, y1, t1, x2, y2, t2, x3, y3, t3 = inputs

        tmp_test_case.input = {'x1': x1, 'y1': y1, 't1': t1,
                               'x2': x2, 'y2': y2, 't2': t2,
                               'x3': x3, 'y3': y3, 't3': t3}

        # Solve the problem with this TestCase so we have our own solution, and extract the solution.
        self.solve_test_case(tmp_test_case)
        x = tmp_test_case.output['x']
        y = tmp_test_case.output['y']

        # Extract user solution.
        outputs = list(map(float, user_output_str.split()))
        user_x = outputs[0]
        user_y = outputs[1]

        # Compare our solution with user's solution.
        error_tol = self.testing['error_tol']
        error_distance = math.sqrt((x - user_x)**2 + (y - user_y)**2)  # [km]

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
