import logging
import numpy as np
from problems.test_case import TestCase, TestCaseTypeEnum

logger = logging.getLogger(__name__)


class TestCaseI1Type(TestCaseTypeEnum):
    EARTH = ('Earth', '', 1)
    MOON = ('Moon', '', 1)
    JUPITER = ('Jupiter', '', 1)
    PLUTO = ('Pluto', '', 1)
    PHOBOS = ('Phobos', '', 1)
    # TITAN = ('Titan', '', 1)
    # HALLEY = ('Halley\'s comet', '', 1)
    RANDOM = ('Random', '', 1)


class TestCaseI1(TestCase):
    def input_str(self) -> str:
        return str(self.input['v'])

    def output_str(self) -> str:
        return str(self.output['m_fuel'])


TEST_CASE_TYPE_ENUM = TestCaseI1Type
TEST_CASE_CLASS = TestCaseI1

PHYSICAL_CONSTANTS = {
    # TODO: get actual values.
    'v_e': 250,  # [m/s]
    'M': 12000  # [kg]
}
TESTING_CONSTANTS = {
    'error_tol': 0.001  # [kg]
}


def generate_input(test_type: TestCaseI1Type) -> TestCaseI1:
    test_case = TestCaseI1(test_type)

    if test_type is TestCaseI1Type.EARTH:
        v = 11.186
    elif test_type is TestCaseI1Type.MOON:
        v = 2.38
    elif test_type is TestCaseI1Type.JUPITER:
        v = 60.20
    elif test_type is TestCaseI1Type.PLUTO:
        v = 1.23
    elif test_type is TestCaseI1Type.PHOBOS:
        v = 0.001139
    elif test_type is TestCaseI1Type.RANDOM:
        v = np.random.uniform(1.0, 100.0, 1)[0]

    test_case.input['v'] = v
    return test_case


def solve_test_case(test_case: TestCaseI1) -> None:
    v = test_case.input['v']
    M = PHYSICAL_CONSTANTS['M']
    v_e = PHYSICAL_CONSTANTS['v_e']

    test_case.output['m_fuel'] = M*(np.exp(v/v_e) - 1)
    return


def verify_user_solution(user_input_str: str, user_output_str: str) -> bool:
    logger.info("Verifying user solution...")
    logger.debug("User input string: %s", user_input_str)
    logger.debug("User output string: %s", user_output_str)

    # Build TestCase object out of user's input string.
    tmp_test_case = TestCaseI1(TestCaseI1Type.RANDOM)

    v = float(user_input_str)
    tmp_test_case.input = {'v': v}

    # Solve the problem with this TestCase so we have our own solution, and extract the solution.
    solve_test_case(tmp_test_case)
    m_fuel = tmp_test_case.output['m_fuel']

    # Extract user solution.
    user_m_fuel = float(user_output_str)

    # Compare our solution with user's solution.
    error_tol = TESTING_CONSTANTS['error_tol']
    error_m_fuel = np.abs(m_fuel - user_m_fuel)  # [kg]

    logger.debug("User solution:")
    logger.debug("m_fuel = %f", user_m_fuel)
    logger.debug("Engine solution:")
    logger.debug("m_fuel = %f", m_fuel)
    logger.debug("Error tolerance = %e. Error m_fuel: %e.", error_tol, error_m_fuel)

    if error_m_fuel < error_tol:
        logger.info("User solution correct within error margin.")
        return True
    else:
        logger.info("User solution incorrect within error margin.")
        return False
