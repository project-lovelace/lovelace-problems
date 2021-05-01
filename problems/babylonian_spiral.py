import logging

from numpy.random import randint

from problems.test_case import TestCase, TestCaseTypeEnum
from problems.solutions.babylonian_spiral import babylonian_spiral

logger = logging.getLogger(__name__)

FUNCTION_NAME = "babylonian_spiral"
INPUT_VARS = ["n_steps"]
OUTPUT_VARS = ["x", "y"]

STATIC_RESOURCES = []

PHYSICAL_CONSTANTS = {}
ATOL = {}
RTOL = {}


class TestCaseType(TestCaseTypeEnum):
    FEW_STEPS = ("few steps", 3)
    MANY_STEPS = ("many steps", 2)


class ProblemTestCase(TestCase):
    def input_tuple(self):
        return self.input["n_steps"],

    def output_tuple(self) -> tuple:
        return (self.output["x"], self.output["y"])


def generate_test_case(test_type):
    test_case = ProblemTestCase(test_type)

    if test_type is TestCaseType.FEW_STEPS:
        n = randint(0, 20)

    elif test_type is TestCaseType.MANY_STEPS:
        n = randint(20, 1000)

    else:
        raise ValueError(f"Unrecognized test case: {test_type}")

    x, y = babylonian_spiral(n)

    test_case.input["n_steps"] = n
    test_case.output = {"x": x, "y": y}

    return test_case
