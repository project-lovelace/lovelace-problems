import logging
import numpy as np
from problems.test_case import TestCase, TestCaseTypeEnum

logger = logging.getLogger(__name__)


class TestCaseI3Type(TestCaseTypeEnum):
    DEATH = ('death', '', 1)
    QUICK_STABLE = ('quick stable', '', 1)
    FLUCTUATE_STABLE = ('fluctuate stable', '', 1)
    OSCILLATION = ('oscillation', '', 1)
    CHAOS = ('chaos', '', 1)
    DIVERGENCE = ('divergence', '', 1)
    UNKNOWN = ('unknown case', '', 0)


class TestCaseI3(TestCase):
    def input_str(self) -> str:
        return str(self.input['r'])

    def output_str(self) -> str:
        return '\n'.join(map(str, self.output['x']))


TEST_CASE_TYPE_ENUM = TestCaseI3Type
TEST_CASE_CLASS = TestCaseI3

PHYSICAL_CONSTANTS = {}
TESTING_CONSTANTS = {
    'error_total_tol': 0.0001
}


def generate_input(test_type: TestCaseI3Type) -> TestCaseI3:
    test_case = TestCaseI3(test_type)

    if test_type is TestCaseI3Type.DEATH:
        r = 1
    elif test_type is TestCaseI3Type.QUICK_STABLE:
        r = 2
    elif test_type is TestCaseI3Type.FLUCTUATE_STABLE:
        r = 3
    elif test_type is TestCaseI3Type.OSCILLATION:
        r = 4
    elif test_type is TestCaseI3Type.CHAOS:
        r = 3.5
    elif test_type is TestCaseI3Type.DIVERGENCE:
        r = 3.6

    test_case.input['r'] = r
    return test_case


def solve_test_case(test_case: TestCaseI3) -> None:
    r = test_case.input['r']

    x = [0.5]
    for _ in range(50):
        x.append(r*x[-1]*(1-x[-1]))

    test_case.output['x'] = x
    return


def verify_user_solution(user_input_str: str, user_output_str: str) -> bool:
    logger.info("Verifying user solution...")
    logger.debug("User input string: %s", user_input_str)
    logger.debug("User output string: %s", user_output_str)
    # Build TestCase object out of user's input string.
    tmp_test_case = TestCaseI3(TestCaseI3Type.UNKNOWN)

    r = float(user_input_str)
    tmp_test_case.input = {'r': r}

    # Solve the problem with this TestCase so we have our own solution, and extract the solution.
    solve_test_case(tmp_test_case)
    x = tmp_test_case.output['x']

    # Extract user solution.
    user_x = list(map(float, user_output_str.split()))

    # TODO: Assert that u and user_x are of the same size!

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

    if error_x < error_total_tol:
        logger.info("User solution correct within error margin.")
        return True
    else:
        logger.info("User solution incorrect within error margin.")
        return False
