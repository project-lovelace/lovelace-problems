import math
import random
import logging

import numpy as np

from problems.test_case import TestCase, TestCaseTypeEnum
from problems.solutions.definite_integrals import area_of_rectangles

logger = logging.getLogger(__name__)


class TestCaseType(TestCaseTypeEnum):
    ZERO = ("Zero function (rectangles with no height)", 1)
    CONSTANT = ("Constant function (all rectangles have the same height)", 1)
    EXPONENTIAL = ("Exponential function", 1)


class ProblemTestCase(TestCase):
    def input_tuple(self) -> tuple:
        return self.input["rectangle_heights"], self.input["rectangle_width"]

    def output_tuple(self) -> tuple:
        return (self.output["area"],)


TEST_CASE_TYPE_ENUM = TestCaseType
TEST_CASE_CLASS = ProblemTestCase
FUNCTION_NAME = "area_of_rectangles"
STATIC_RESOURCES = []

PHYSICAL_CONSTANTS = {}

TESTING_CONSTANTS = {
    "rel_tol": 1e-6
}


def generate_test_case(test_type: TestCaseType) -> ProblemTestCase:
    test_case = ProblemTestCase(test_type)

    if test_type is TestCaseType.ZERO:
        N = random.randint(5, 10)
        f = [0 for _ in range(N)]
        dx = 1
    elif test_type is TestCaseType.CONSTANT:
        N = random.randint(5, 10)
        c = random.uniform(-5, 5)
        f = [c for _ in range(N)]
        dx = 1
    elif test_type is TestCaseType.EXPONENTIAL:
        N = random.randint(20, 40)
        x1, x2 = 0, random.uniform(3, 5)
        dx = (x2 - x1) / N
        f = [math.exp(x) for x in np.linspace(x1, x2, N)]
    else:
        raise ValueError("Invalid test case type.")

    test_case.input = {
        "rectangle_heights": f,
        "rectangle_width": dx}

    return test_case


def solve_test_case(test_case: ProblemTestCase) -> None:
    f, dx = test_case.input["f"], test_case.input["dx"]
    test_case.output["area"] = area_of_rectangles(f, dx)
    return


def verify_user_solution(user_input: tuple, user_output: tuple) -> bool:
    logger.info("Verifying user solution...")
    logger.debug("User input tuple: %s", user_input)
    logger.debug("User output tuple: %s", user_output)

    tmp_test_case = ProblemTestCase()

    f, dx = user_input

    tmp_test_case.input = {"f": f, "dx": dx}

    solve_test_case(tmp_test_case)
    area = tmp_test_case.output["area"]

    user_area = user_output[0]

    logger.debug("User solution:")
    logger.debug("area = {:g}".format(user_area))
    logger.debug("Engine solution:")
    logger.debug("area = {:g}".format(area))
    logger.debug("Relative tolerance = {:g}.".format(TESTING_CONSTANTS["rel_tol"]))

    passed = False

    if math.isclose(area, user_area, rel_tol=TESTING_CONSTANTS["rel_tol"]):
        logger.info("User solution correct.")
        passed = True
    else:
        logger.info("User solution is wrong.")
        passed = False

    return passed, str(area)
