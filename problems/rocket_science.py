import logging
import importlib

import numpy as np

from problems.test_case import TestCase, TestCaseTypeEnum
from problems.solutions.rocket_science import rocket_fuel

logger = logging.getLogger(__name__)


class TestCaseType(TestCaseTypeEnum):
    EARTH = ('Earth', 1)
    MOON = ('Moon', 1)
    JUPITER = ('Jupiter', 1)
    PLUTO = ('Pluto', 1)
    PHOBOS = ('Phobos', 1)
    RANDOM = ('Random', 1)


class ProblemTestCase(TestCase):
    def input_tuple(self) -> tuple:
        return (self.input['v'],)

    def output_tuple(self) -> tuple:
        return (self.output['m_fuel'],)


FUNCTION_NAME = "rocket_fuel"
STATIC_RESOURCES = []

PHYSICAL_CONSTANTS = {
    'v_e': 2550,  # [m/s]
    'M': 250000   # [kg]
}

TESTING_CONSTANTS = {
    'error_rel_tol': 1e-6
}


def generate_test_case(test_type: TestCaseType) -> ProblemTestCase:
    test_case = ProblemTestCase(test_type)

    if test_type is TestCaseType.EARTH:
        v = 11186
    elif test_type is TestCaseType.MOON:
        v = 2380
    elif test_type is TestCaseType.JUPITER:
        v = 60200
    elif test_type is TestCaseType.PLUTO:
        v = 1230
    elif test_type is TestCaseType.PHOBOS:
        v = 1.139
    elif test_type is TestCaseType.RANDOM:
        v = float(np.random.uniform(1.0, 100.0, 1)[0])

    test_case.input['v'] = v
    return test_case


def solve_test_case(test_case: ProblemTestCase) -> None:
    v = test_case.input['v']
    test_case.output['m_fuel'] = rocket_fuel(v)
    return


def verify_user_solution(user_input: tuple, user_output: tuple) -> bool:
    logger.info("Verifying user solution...")
    logger.debug("User input tuple: %s", user_input)
    logger.debug("User output tuple: %s", user_output)

    # Build TestCase object out of user's input string.
    tmp_test_case = ProblemTestCase()

    v = user_input[0]
    tmp_test_case.input = {'v': v}

    # Solve the problem with this TestCase so we have our own solution, and extract the solution.
    solve_test_case(tmp_test_case)
    m_fuel = tmp_test_case.output['m_fuel']

    # Extract user solution.
    user_m_fuel = user_output[0]

    # Compare our solution with user's solution.
    error_rel_tol = TESTING_CONSTANTS['error_rel_tol']
    error_rel_m_fuel = np.abs(m_fuel - user_m_fuel) / m_fuel

    logger.debug("User solution:")
    logger.debug("m_fuel = %f", user_m_fuel)
    logger.debug("Engine solution:")
    logger.debug("m_fuel = %f", m_fuel)
    logger.debug("Error relative tolerance = %e. Error m_fuel: %e.", error_rel_tol, error_rel_m_fuel)

    passed = False

    if error_rel_m_fuel < error_rel_tol:
        logger.info("User solution correct within error margin of {:g}.".format(error_rel_tol))
        passed = True
    else:
        logger.info("User solution incorrect.")

    return passed, str(m_fuel)
