import math
import logging

import numpy as np

from problems.test_case import TestCase, TestCaseTypeEnum

logger = logging.getLogger(__name__)


class TestCaseType(TestCaseTypeEnum):
    SMALL_N = ("1 < n < 10", 2)


class ProblemTestCase(TestCase):
    def input_tuple(self) -> tuple:
        return (self.input["N"],)

    def output_tuple(self) -> tuple:
        return (self.output["pi"],)


TEST_CASE_TYPE_ENUM = TestCaseType
TEST_CASE_CLASS = ProblemTestCase
FUNCTION_NAME = "pi"
STATIC_RESOURCES = []

PHYSICAL_CONSTANTS = {}
TESTING_CONSTANTS = {
    "rel_tol": 1e-5
}


def generate_test_case(test_type: TestCaseType) -> ProblemTestCase:
    test_case = ProblemTestCase(test_type)

    if test_type is TestCaseType.SMALL_N:
        N = np.random.uniform(2, 10)
    else:
        raise ValueError("Invalid test case type.")

    test_case.input["N"] = N

    return test_case


def solve_test_case(test_case: ProblemTestCase) -> None:
    N = test_case.input["N"]

    test_case.output["pi"] = 4 * sum([(-1) ** k / (2*k + 1) for k in range(N)])
    return


def verify_user_solution(user_input: tuple, user_output: tuple) -> bool:
    logger.info("Verifying user solution...")
    logger.debug("User input tuple: %s", user_input)
    logger.debug("User output tuple: %s", user_output)

    tmp_test_case = ProblemTestCase()

    N = user_input[0]

    solve_test_case(tmp_test_case)
    pi = tmp_test_case.output["pi"]

    user_pi = user_output[0]

    logger.debug("User solution:")
    logger.debug("distance = {:d}".format(user_pi))
    logger.debug("Engine solution:")
    logger.debug("distance = {:d}".format(pi))
    logger.debug("Relative tolerance = {:g}.".format(TESTING_CONSTANTS["rel_tol"]))

    passed = False

    if math.isclose(pi, user_pi, rel_tol=TESTING_CONSTANTS["rel_tol"]):
        logger.info("User solution correct.")
        passed = True
    else:
        logger.info("User solution is wrong.")
        passed = False

    return passed, str(pi)
