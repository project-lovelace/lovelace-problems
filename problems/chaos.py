import logging
from typing import Tuple

from problems.test_case import TestCase, TestCaseTypeEnum, test_case_solution_correct
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

    def output_str(self) -> str:
        return str(self.output['x'])


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

    test_case.input['r'] = float(r)
    test_case.output['x'] = logistic_map(r)

    return test_case


def verify_user_solution(correct_test_case: TestCase, user_input: tuple, user_output: tuple) -> Tuple[bool, str]:
    user_test_case = ProblemTestCase(None, INPUT_VARS, user_input, OUTPUT_VARS, user_output)
    passed, correct_test_case = test_case_solution_correct(correct_test_case, user_test_case, ATOL, RTOL)
    return passed, correct_test_case.output_tuple()
