import logging

import numpy as np

from problems.test_case import TestCase, TestCaseTypeEnum

logger = logging.getLogger(__name__)


class TestCase1Type(TestCaseTypeEnum):
    EARTH = ('Earth', 1)
    MOON = ('Moon', 1)
    JUPITER = ('Jupiter', 1)
    PLUTO = ('Pluto', 1)
    PHOBOS = ('Phobos', 1)
    RANDOM = ('Random', 1)


class TestCase1(TestCase):
    def input_tuple(self) -> tuple:
        return (self.input['v'],)

    def output_tuple(self) -> tuple:
        return (self.output['m_fuel'],)


TEST_CASE_TYPE_ENUM = TestCase1Type
TEST_CASE_CLASS = TestCase1

RESOURCES = []

PHYSICAL_CONSTANTS = {
    'v_e': 2550,  # [m/s]
    'M': 250000   # [kg]
}

TESTING_CONSTANTS = {
    'error_tol': 0.001  # [kg]
}


def generate_test_case(test_type: TestCase1Type) -> TestCase1:
    test_case = TestCase1(test_type)

    if test_type is TestCase1Type.EARTH:
        v = 11186
    elif test_type is TestCase1Type.MOON:
        v = 2380
    elif test_type is TestCase1Type.JUPITER:
        v = 60200
    elif test_type is TestCase1Type.PLUTO:
        v = 1230
    elif test_type is TestCase1Type.PHOBOS:
        v = 1.139
    elif test_type is TestCase1Type.RANDOM:
        v = float(np.random.uniform(1.0, 100.0, 1)[0])

    test_case.input['v'] = v
    return test_case


def solve_test_case(test_case: TestCase1) -> None:
    v = test_case.input['v']
    M = PHYSICAL_CONSTANTS['M']
    v_e = PHYSICAL_CONSTANTS['v_e']

    test_case.output['m_fuel'] = M*(np.exp(v/v_e) - 1)
    return


def verify_user_solution(user_input: tuple, user_output: tuple) -> bool:
    logger.info("Verifying user solution...")
    logger.debug("User input tuple: %s", user_input)
    logger.debug("User output tuple: %s", user_output)

    # Build TestCase object out of user's input string.
    tmp_test_case = TestCase1()

    v = user_input[0]
    tmp_test_case.input = {'v': v}

    # Solve the problem with this TestCase so we have our own solution, and extract the solution.
    solve_test_case(tmp_test_case)
    m_fuel = tmp_test_case.output['m_fuel']

    # Extract user solution.
    user_m_fuel = user_output[0]

    # Compare our solution with user's solution.
    error_tol = TESTING_CONSTANTS['error_tol']
    error_m_fuel = np.abs(m_fuel - user_m_fuel)  # [kg]

    logger.debug("User solution:")
    logger.debug("m_fuel = %f", user_m_fuel)
    logger.debug("Engine solution:")
    logger.debug("m_fuel = %f", m_fuel)
    logger.debug("Error tolerance = %e. Error m_fuel: %e.", error_tol, error_m_fuel)

    if error_m_fuel < error_tol:
        logger.info("User solution correct within error margin of {:g}.".format(error_tol))
        return True
    else:
        logger.info("User solution incorrect.")
        return False
