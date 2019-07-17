import logging
from typing import Tuple

from numpy.random import uniform

from problems.test_case import TestCase, TestCaseTypeEnum, test_case_solution_correct
from problems.solutions.babylonian_square_roots import babylonian_sqrt

logger = logging.getLogger(__name__)

FUNCTION_NAME = "babylonian_sqrt"
INPUT_VARS = ['n']
OUTPUT_VARS = ['sqrt_n']

STATIC_RESOURCES = []

PHYSICAL_CONSTANTS = {}
ATOL = {}
RTOL = {
    'sqrt_n': 1e-10
}


class TestCaseType(TestCaseTypeEnum):
    ZERO = ("Zero", 1)
    NEGATIVE = ("Negative", 1)
    SMALL_POSITIVE = ("1 < n < 10", 2)


class ProblemTestCase(TestCase):
    def input_tuple(self) -> tuple:
        return self.input['n'],

    def output_tuple(self) -> tuple:
        return self.output['sqrt_n'],

    def output_str(self) -> str:
        return str(self.output['sqrt_n'])


def generate_test_case(test_type: TestCaseType) -> ProblemTestCase:
    test_case = ProblemTestCase(test_type)

    if test_type is TestCaseType.ZERO:
        n = 0

    elif test_type is TestCaseType.NEGATIVE:
        n = uniform(-10, -0.01)

    elif test_type is TestCaseType.SMALL_POSITIVE:
        n = uniform(1, 10)

    test_case.input['n'] = n
    return test_case


def solve_test_case(test_case: ProblemTestCase) -> None:
    n = test_case.input['n']
    test_case.output['sqrt_n'] = babylonian_sqrt(n)


def verify_user_solution(user_input: tuple, user_output: tuple) -> Tuple[bool, str]:
    user_test_case = ProblemTestCase(None, INPUT_VARS, user_input, OUTPUT_VARS, user_output)
    passed, correct_test_case = test_case_solution_correct(user_test_case, ATOL, RTOL, ProblemTestCase, solve_test_case)
    return passed, correct_test_case.output_str()
