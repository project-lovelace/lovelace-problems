import logging

import numpy as np

from problems.test_case import TestCase, TestCaseTypeEnum
from problems.solutions.chaos import logistic_map

logger = logging.getLogger(__name__)


class TestCase3Type(TestCaseTypeEnum):
    DEATH = ('death', 1)
    QUICK_STABLE = ('quick stable', 1)
    FLUCTUATE_STABLE = ('fluctuate stable', 1)
    OSCILLATION = ('oscillation', 1)
    CHAOS = ('chaos', 1)
    DIVERGENCE = ('divergence', 1)


class TestCase3(TestCase):
    def input_tuple(self) -> tuple:
        return (self.input['r'],)

    def output_tuple(self) -> tuple:
        return (self.output['x'],)


TEST_CASE_TYPE_ENUM = TestCase3Type
TEST_CASE_CLASS = TestCase3
FUNCTION_NAME = "logistic_map"
STATIC_RESOURCES = []

PHYSICAL_CONSTANTS = {}
TESTING_CONSTANTS = {
    'error_total_tol': 0.0001
}


def generate_test_case(test_type: TestCase3Type) -> TestCase3:
    test_case = TestCase3(test_type)

    if test_type is TestCase3Type.DEATH:
        r = 1
    elif test_type is TestCase3Type.QUICK_STABLE:
        r = 2
    elif test_type is TestCase3Type.FLUCTUATE_STABLE:
        r = 3
    elif test_type is TestCase3Type.OSCILLATION:
        r = 4
    elif test_type is TestCase3Type.CHAOS:
        r = 3.5
    elif test_type is TestCase3Type.DIVERGENCE:
        r = 3.6

    test_case.input['r'] = r
    return test_case


def solve_test_case(test_case: TestCase3) -> None:
    r = test_case.input['r']
    test_case.output['x'] = logistic_map(r)
    return


def verify_user_solution(user_input: tuple, user_output: tuple) -> bool:
    logger.info("Verifying user solution...")
    logger.debug("User input: %s", user_input)
    logger.debug("User output: %s", user_output)

    # Build TestCase object out of user's input string.
    tmp_test_case = TestCase3()

    r = user_input[0]
    tmp_test_case.input = {'r': r}

    # Solve the problem with this TestCase so we have our own solution, and extract the solution.
    solve_test_case(tmp_test_case)
    x = tmp_test_case.output['x']

    # Extract user solution.
    user_x = user_output[0]

    if len(x) != len(user_x):
        return False, x

    # Compare our solution with user's solution.
    error_total_tol = TESTING_CONSTANTS['error_total_tol']
    error_x = 0
    for i in range(len(x)):
        error_x += np.abs(x[i] - user_x[i])

    logger.debug("User solution:")
    logger.debug("x = {}".format(user_x))
    logger.debug("Engine solution:")
    logger.debug("x = {}".format(x))
    logger.debug("Error tolerance = %e. Error x: %e.", error_total_tol, error_x)

    passed = False

    if error_x < error_total_tol:
        logger.info("User solution correct within error margin of {:g}.".format(error_total_tol))
        passed = True
    else:
        logger.info("User solution incorrect within error margin.")

    return passed, x
