import math
import random
import logging

import numpy as np

from problems.test_case import TestCase, TestCaseTypeEnum

logger = logging.getLogger(__name__)


class TestCaseType(TestCaseTypeEnum):
    ZERO = ("Zero", 1)
    NEGATIVE = ("Negative", 1)
    SMALL_POSITIVE = ("1 < n < 10", 2)


class ProblemTestCase(TestCase):
    def input_tuple(self) -> tuple:
        return self.input["n"]

    def output_tuple(self) -> tuple:
        return (self.output["sqrt_n"],)


TEST_CASE_TYPE_ENUM = TestCaseType
TEST_CASE_CLASS = ProblemTestCase
FUNCTION_NAME = "babylonian_sqrt"
STATIC_RESOURCES = []

PHYSICAL_CONSTANTS = {}

TESTING_CONSTANTS = {
    "rel_tol": 1e-10
}


def generate_test_case(test_type: TestCaseType) -> ProblemTestCase:
    test_case = ProblemTestCase(test_type)

    if test_type is TestCaseType.ZERO:
        n = 0
    elif test_type is TestCaseType.NEGATIVE:
        n = random.uniform(-10, -0.01)
    elif test_type is TestCaseType.SMALL_POSITIVE:
        n = random.uniform(1, 10)
    else:
        raise ValueError("Invalid test case type.")

    return test_case


def solve_test_case(test_case: ProblemTestCase) -> None:
    def babylonian_sqrt(S):
        if S == 0:
            return 0

        if S < 0:
            return "invalid"

        x_n = 10
        while abs(x_n ** 2 - S) / S > 1e-10:
            x_n = 0.5 * (x_n + S / x_n)

        return x_n

    n = test_case.input["n"]
    test_case.output["sqrt_n"] = babylonian_sqrt(n)
    return


def verify_user_solution(user_input: tuple, user_output: tuple) -> bool:
    logger.info("Verifying user solution...")
    logger.debug("User input tuple: %s", user_input)
    logger.debug("User output tuple: %s", user_output)

    tmp_test_case = ProblemTestCase()

    n = user_input[0]

    tmp_test_case.input["n"] = n

    solve_test_case(tmp_test_case)
    sqrt_n = tmp_test_case.output["sqrt_n"]

    user_sqrt_n = user_output[0]

    logger.debug("User solution:")
    logger.debug("sqrt_n = {:g}".format(user_sqrt_n))
    logger.debug("Engine solution:")
    logger.debug("sqrt_n = {:g}".format(sqrt_n))
    logger.debug("Relative tolerance = {:g}.".format(TESTING_CONSTANTS["rel_tol"]))

    passed = False

    if math.isclose(sqrt_n, user_sqrt_n, rel_tol=TESTING_CONSTANTS["rel_tol"]):
        logger.info("User solution correct.")
        passed = True
    else:
        logger.info("User solution is wrong.")
        passed = False

    return passed, str(sqrt_n)
