import math
import logging

import numpy as np

from problems.test_case import TestCase, TestCaseTypeEnum

logger = logging.getLogger(__name__)


class TestCaseType(TestCaseTypeEnum):
    WARM_DAY = ("Warm day", 1)
    COLD_DAY = ("Cold day", 1)
    WATER_FREEZING_POINT = ("Freezing point of water", 1)
    WATER_BOILING_POINT = ("Boiling point of water", 1)
    MINUS_40 = ("-40°C", 1)
    ABSOLUTE_ZERO = ("Absolute zero", 1)
    SUN_SURFACE = ("Surface of the sun", 1)


class ProblemTestCase(TestCase):
    def input_tuple(self) -> tuple:
        return self.input["F"]

    def output_tuple(self) -> tuple:
        return self.output["C"]


TEST_CASE_TYPE_ENUM = TestCaseType
TEST_CASE_CLASS = ProblemTestCase
FUNCTION_NAME = "celcius"
STATIC_RESOURCES = []

PHYSICAL_CONSTANTS = {}
TESTING_CONSTANTS = {
    "rel_tol": 1e-5
}


def generate_test_case(test_type: TestCaseType) -> ProblemTestCase:
    test_case = ProblemTestCase(test_type)

    if test_type is TestCaseType.WARM_DAY:
        F = np.random.uniform(80, 110)
    elif test_type is TestCaseType.COLD_DAY:
        F = np.random.uniform(-20, 30)
    elif test_type is TestCaseType.WATER_FREEZING_POINT:
        F = 32
    elif test_type is TestCaseType.WATER_BOILING_POINT:
        F = 212
    elif test_type is TestCaseType.MINUS_40:
        F = -40
    elif test_type is TestCaseType.ABSOLUTE_ZERO:
        F = -459.67
    elif test_type is TestCaseType.SUN_SURFACE:
        F = 9940.73
    else:
        raise ValueError("Invalid test case type.")

    test_case.input["F"] = F

    return test_case


def solve_test_case(test_case: ProblemTestCase) -> None:
    F = test_case.input["F"]
    test_case.output["C"] = (5/9) * (F - 32)
    return


def verify_user_solution(user_input: tuple, user_output: tuple) -> bool:
    logger.info("Verifying user solution...")
    logger.debug("User input tuple: %s", user_input)
    logger.debug("User output tuple: %s", user_output)

    tmp_test_case = ProblemTestCase()

    F = user_input[0]
    tmp_test_case.input = {"F": F}

    solve_test_case(tmp_test_case)
    C = tmp_test_case.output["C"]

    user_C = user_output[0]

    logger.debug("User solution:")
    logger.debug("C = {:f}".format(user_C))
    logger.debug("Engine solution:")
    logger.debug("C = {:f}".format(C))
    logger.debug("Relative tolerance = {:g}.".format(TESTING_CONSTANTS["rel_tol"]))

    passed = False

    if math.isclose(C, user_C, rel_tol=TESTING_CONSTANTS["rel_tol"]):
        logger.info("User solution correct.")
        passed = True
    else:
        logger.info("User solution is wrong.")
        passed = False

    return passed, str(C)
