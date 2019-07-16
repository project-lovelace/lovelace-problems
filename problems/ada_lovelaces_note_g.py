import logging

import numpy as np
from fractions import Fraction
from math import factorial

from problems.test_case import TestCase, TestCaseTypeEnum
from problems.solutions.ada_lovelaces_note_g import bernoulli

logger = logging.getLogger(__name__)


class TestCaseType(TestCaseTypeEnum):
    ZEROTH = ("Zeroth Bernoulli number", 1)
    FIRST = ("First Bernoulli number", 1)
    SECOND = ("Second Bernoulli number", 1)
    THIRD = ("Third Bernoulli number", 1)
    RANDOM_EVEN = ("Even n > 2", 2)
    RANDOM_ODD = ("Odd n > 3", 2)
    LARGE_EVEN = ("Even n > 250", 1)
    LARGE_ODD = ("Odd n > 250", 1)


class ProblemTestCase(TestCase):
    def input_tuple(self) -> tuple:
        return (self.input['n'],)

    def output_tuple(self) -> tuple:
        numerator = self.output["numerator"]
        denominator = self.output["denominator"]
        return numerator, denominator


FUNCTION_NAME = "bernoulli"
STATIC_RESOURCES = []

PHYSICAL_CONSTANTS = {}
TESTING_CONSTANTS = {}


def generate_test_case(test_type: TestCaseType) -> ProblemTestCase:
    test_case = ProblemTestCase(test_type)

    if test_type is TestCaseType.ZEROTH:
        n = 0
    elif test_type is TestCaseType.FIRST:
        n = 1
    elif test_type is TestCaseType.SECOND:
        n = 2
    elif test_type is TestCaseType.THIRD:
        n = 3
    elif test_type is TestCaseType.RANDOM_EVEN:
        n = 2 * np.random.randint(2, 50)
    elif test_type is TestCaseType.RANDOM_ODD:
        n = 2 * np.random.randint(2, 50) + 1
    elif test_type is TestCaseType.LARGE_EVEN:
        n = 2 * np.random.randint(125, 250)
    elif test_type is TestCaseType.LARGE_ODD:
        n = 2 * np.random.randint(125, 250) + 1

    test_case.input['n'] = n
    return test_case


def solve_test_case(test_case: ProblemTestCase) -> None:
    n = test_case.input["n"]
    test_case.output["B_n_numerator"], test_case.output["B_n_denominator"] = bernoulli(n)
    return


def verify_user_solution(user_input: tuple, user_output: tuple) -> bool:
    logger.info("Verifying user solution...")
    logger.debug("User input: %s", user_input)
    logger.debug("User output: %s", user_output)

    # Build TestCase object out of user's input string.
    tmp_test_case = ProblemTestCase()

    n = user_input[0]
    tmp_test_case.input = {"n": n}

    # Solve the problem with this TestCase so we have our own solution, and extract the solution.
    solve_test_case(tmp_test_case)
    B_n_numerator = tmp_test_case.output['B_n_numerator']
    B_n_denominator = tmp_test_case.output['B_n_denominator']

    # Extract user solution.
    user_B_n_numerator = user_output[0]
    user_B_n_denominator = user_output[1]

    logger.debug("User solution:")
    logger.debug("B_n_numerator = %d, B_n_denominator = %d", user_B_n_numerator, user_B_n_denominator)
    logger.debug("Engine solution:")
    logger.debug("B_n_numerator = %d, B_n_denominator = %d", B_n_numerator, B_n_denominator)

    passed = False

    if user_B_n_numerator == B_n_numerator and user_B_n_denominator == B_n_denominator:
        logger.info("User solution correct.")
        passed = True
    else:
        logger.info("User solution is wrong.")

    return passed, "B_n_numerator = {:d}, B_n_denominator = {:d}".format(B_n_numerator, B_n_denominator)