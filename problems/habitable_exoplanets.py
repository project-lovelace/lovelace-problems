import numpy as np

from problems.test_case import TestCase, TestCaseTypeEnum

from os import path
import logging.config
import logging


logging_config_path = path.join(path.dirname(path.abspath(__file__)), '..', 'logging.ini')
logging.config.fileConfig(logging_config_path)
logger = logging.getLogger(__name__)


class TestCaseI2Type(TestCaseTypeEnum):
    EARTH = ('Earth', '', 1)
    PROXIMA_CENTAURI_b = ('Proxima Centauri b', '', 1)
    KEPLER_440b = ('Kepler 440b', '', 1)
    RANDOM = ('Randomly generated exoplanet', '', 1)
    UNKNOWN = ('unknown case', 0)


class TestCaseI2(TestCase):
    def input_str(self) -> str:
        return str(self.input['L_star']) + '\n' + str(self.input['r'])

    def output_str(self) -> str:
        return self.output['habitability']


TEST_CASE_TYPE_ENUM = TestCaseI2Type
TEST_CASE_CLASS = TestCaseI2

PHYSICAL_CONSTANTS = {}
TESTING_CONSTANTS = {}


def generate_input(test_type: TestCaseI2Type) -> TestCaseI2:
    test_case = TestCaseI2(test_type)

    if test_type is TestCaseI2Type.EARTH:
        L_star = 1.00
        r = 1.00
    elif test_type is TestCaseI2Type.PROXIMA_CENTAURI_b:
        L_star = 1.00
        r = 1.00
    elif test_type is TestCaseI2Type.KEPLER_440b:
        L_star = 1.43
        r = 0.242
    elif test_type is TestCaseI2Type.RANDOM:
        L_star = np.random.uniform(0.1, 5.0, 1)
        r = np.random.uniform(0.1, 5.0, 1)

    test_case.input['L_star'] = L_star
    test_case.input['r'] = r
    return test_case


def solve_test_case(test_case: TestCaseI2) -> None:
    L_star = test_case.input['L_star']
    r = test_case.input['r']

    if r < np.sqrt(L_star/1.1):
        test_case.output['habitability'] = 'too hot'
    elif r > np.sqrt(L_star/0.53):
        test_case.output['habitability'] = 'too cold'
    else:
        test_case.output['habitability'] = 'just right'

    return


def verify_user_solution(user_input_str: str, user_output_str: str) -> bool:
    logger.info("Verifying user solution...")
    logger.debug("User input string: %s", user_input_str)
    logger.debug("User output string: %s", user_output_str)

    # Build TestCase object out of user's input string.
    tmp_test_case = TestCaseI2(TestCaseI2Type.UNKNOWN)

    inputs = list(map(float, user_input_str.split()))
    L_star, r = inputs
    tmp_test_case.input = {'L_star': L_star, 'r': r}

    # Solve the problem with this TestCase so we have our own solution, and extract the solution.
    solve_test_case(tmp_test_case)
    habitability = tmp_test_case.output['habitability']

    # Extract user solution.
    outputs = list(map(float, user_output_str.split()))
    user_habitability = outputs[0]

    logger.debug("User solution:")
    logger.debug("habitability = %s", user_habitability)
    logger.debug("Our solution:")
    logger.debug("habitability = %s", habitability)

    if habitability == user_habitability:
        logger.info("User solution correct.")
        return True
    else:
        logger.info("User solution incorrect.")
        return False
