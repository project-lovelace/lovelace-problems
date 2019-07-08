import math
import logging

import numpy as np

from problems.test_case import TestCase, TestCaseTypeEnum

logger = logging.getLogger(__name__)


class TestCaseType(TestCaseTypeEnum):
    COLD_CALM = ("Cold calm weather", 1)
    COLD_WINDY = ("Cold windy weather", 1)
    VERY_COLD_CALM = ("Very cold and calm weather", 1)
    VERY_COLD_WINDY = ("Very cold and windy weather", 1)


class ProblemTestCase(TestCase):
    def input_tuple(self) -> tuple:
        return self.input["T_a"], self.input["v"]

    def output_tuple(self) -> tuple:
        return (self.output["T_wc"],)


TEST_CASE_TYPE_ENUM = TestCaseType
TEST_CASE_CLASS = ProblemTestCase
FUNCTION_NAME = "wind_chill"
STATIC_RESOURCES = []

PHYSICAL_CONSTANTS = {}
TESTING_CONSTANTS = {
    "rel_tol": 1e-5
}


def generate_test_case(test_type: TestCaseType) -> ProblemTestCase:
    test_case = ProblemTestCase(test_type)

    if test_type is TestCaseType.COLD_CALM:
        T_a = np.random.uniform(-15, 2)
        v = np.random.uniform(2, 8)
    elif test_type is TestCaseType.COLD_WINDY:
        T_a = np.random.uniform(-15, 2)
        v = np.random.uniform(25, 60)
    elif test_type is TestCaseType.VERY_COLD_CALM:
        T_a = np.random.uniform(-50, -20)
        v = np.random.uniform(2, 8)
    elif test_type is TestCaseType.VERY_COLD_WINDY:
        T_a = np.random.uniform(-50, -20)
        v = np.random.uniform(25, 60)
    else:
        raise ValueError("Invalid test case type.")

    test_case.input["T_a"], test_case.input["v"] = T_a, v

    return test_case


def solve_test_case(test_case: ProblemTestCase) -> None:
    T_a = test_case.input["T_a"]
    v = test_case.input["v"]

    test_case.output["T_wc"] = 13.12 + 0.6215*T_a - 11.37*v**0.16 + 0.3965*T_a*v**0.16
    return


def verify_user_solution(user_input: tuple, user_output: tuple) -> bool:
    logger.info("Verifying user solution...")
    logger.debug("User input tuple: %s", user_input)
    logger.debug("User output tuple: %s", user_output)

    tmp_test_case = ProblemTestCase()

    T_a, v = user_input
    tmp_test_case.input = {"T_a": T_a, "v": v}

    solve_test_case(tmp_test_case)
    T_wc = tmp_test_case.output["T_wc"]

    user_T_wc = user_output[0]

    logger.debug("User solution:")
    logger.debug("T_wc = {:f}".format(user_T_wc))
    logger.debug("Engine solution:")
    logger.debug("T_wc = {:f}".format(T_wc))
    logger.debug("Relative tolerance = {:g}.".format(TESTING_CONSTANTS["rel_tol"]))

    passed = False

    if math.isclose(T_wc, user_T_wc, rel_tol=TESTING_CONSTANTS["rel_tol"]):
        logger.info("User solution correct.")
        passed = True
    else:
        logger.info("User solution is wrong.")
        passed = False

    return passed, str(T_wc)
