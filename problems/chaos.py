import logging
from typing import Tuple

from problems.test_case import TestCase, TestCaseTypeEnum
from problems.solutions.chaos import logistic_map

logger = logging.getLogger(__name__)

FUNCTION_NAME = "logistic_map"
INPUT_VARS = ['r']
OUTPUT_VARS = ['x']

STATIC_RESOURCES = []

PHYSICAL_CONSTANTS = {}
ATOL = {}
RTOL = {
    'x': 0.0001
}


class TestCaseType(TestCaseTypeEnum):
    DEATH = ('death', 1)
    QUICK_STABLE = ('quick stable', 1)
    FLUCTUATE_STABLE = ('fluctuate stable', 1)
    CHAOS = ('chaos', 1)
    DIVERGENCE = ('divergence', 1)


class ProblemTestCase(TestCase):
    def input_tuple(self) -> tuple:
        return self.input['r'],

    def output_tuple(self) -> tuple:
        return self.output['x'],


def generate_test_case(test_type: TestCaseType) -> ProblemTestCase:
    test_case = ProblemTestCase(test_type)

    if test_type is TestCaseType.DEATH:
        r = 1

    elif test_type is TestCaseType.QUICK_STABLE:
        r = 2

    elif test_type is TestCaseType.FLUCTUATE_STABLE:
        r = 3

    elif test_type is TestCaseType.CHAOS:
        r = 3.5

    elif test_type is TestCaseType.DIVERGENCE:
        r = 3.6

    else:
        raise ValueError(f"Unrecognized test case: {test_type}")

    test_case.input['r'] = float(r)
    test_case.output['x'] = logistic_map(r)

    return test_case
