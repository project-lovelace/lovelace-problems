import logging

import numpy as np

from problems.test_case import TestCase, TestCaseTypeEnum
from problems.solutions.habitable_exoplanets import habitable_exoplanet

logger = logging.getLogger(__name__)


class TestCaseType(TestCaseTypeEnum):
    EARTH = ('Earth', 1)
    PROXIMA_CENTAURI_B = ('Proxima Centauri b', 1)
    KEPLER_440B = ('Kepler 440b', 1)
    RANDOM = ('Randomly generated exoplanet', 1)


class ProblemTestCase(TestCase):
    def input_tuple(self) -> tuple:
        return (self.input['L_star'], self.input['r'])

    def output_tuple(self) -> tuple:
        return (self.output['habitability'],)


TEST_CASE_TYPE_ENUM = TestCaseType
TEST_CASE_CLASS = ProblemTestCase
FUNCTION_NAME = "habitable_exoplanet"
STATIC_RESOURCES = []

PHYSICAL_CONSTANTS = {}
TESTING_CONSTANTS = {}


def generate_test_case(test_type: TestCaseType) -> ProblemTestCase:
    test_case = ProblemTestCase(test_type)

    if test_type is TestCaseType.EARTH:
        L_star = 1.00
        r = 1.00
    elif test_type is TestCaseType.PROXIMA_CENTAURI_B:
        L_star = 1.00
        r = 1.00
    elif test_type is TestCaseType.KEPLER_440B:
        L_star = 1.43
        r = 0.242
    elif test_type is TestCaseType.RANDOM:
        L_star = float(np.random.uniform(0.1, 5.0, 1)[0])
        r = float(np.random.uniform(0.1, 5.0, 1)[0])

    test_case.input['L_star'] = L_star
    test_case.input['r'] = r
    return test_case


def solve_test_case(test_case: ProblemTestCase) -> None:
    L_star = test_case.input['L_star']
    r = test_case.input['r']
    test_case.output['habitability'] = habitable_exoplanet(L_star, r)
    return


def verify_user_solution(user_input: tuple, user_output: tuple) -> bool:
    logger.info("Verifying user solution...")
    logger.debug("User input: %s", user_input)
    logger.debug("User output: %s", user_output)

    # Build TestCase object out of user's input string.
    tmp_test_case = ProblemTestCase()

    L_star, r = user_input
    tmp_test_case.input = {'L_star': L_star, 'r': r}

    # Solve the problem with this TestCase so we have our own solution, and extract the solution.
    solve_test_case(tmp_test_case)
    habitability = tmp_test_case.output['habitability']

    # Extract user solution.
    user_habitability = user_output[0]

    logger.debug("User solution:")
    logger.debug("habitability = %s", user_habitability)
    logger.debug("Our solution:")
    logger.debug("habitability = %s", habitability)

    passed = False

    if habitability == user_habitability:
        logger.info("User solution correct.")
        passed = True
    else:
        logger.info("User solution incorrect.")

    return passed, habitability
