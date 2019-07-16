import logging
from typing import Tuple
from math import exp
from random import randint, uniform
from numpy import linspace

from problems.test_case import TestCase, TestCaseTypeEnum, test_case_solution_correct
from problems.solutions.definite_integrals import area_of_rectangles

logger = logging.getLogger(__name__)


class TestCaseType(TestCaseTypeEnum):
    ZERO = ("Zero function (rectangles with no height)", 1)
    CONSTANT = ("Constant function (all rectangles have the same height)", 1)
    EXPONENTIAL = ("Exponential function", 1)


class ProblemTestCase(TestCase):
    def input_tuple(self) -> tuple:
        return self.input['rectangle_heights'], self.input['rectangle_width']

    def output_tuple(self) -> tuple:
        return self.output['area'],

    def output_str(self) -> str:
        return str(self.output['area'])


FUNCTION_NAME = "area_of_rectangles"
STATIC_RESOURCES = []

INPUT_VARS = ['rectangle_heights', 'rectangle_width']
OUTPUT_VARS = ['area']

PHYSICAL_CONSTANTS = {}
ATOL = {}
RTOL = {
    'area': 1e-6
}


def generate_test_case(test_type: TestCaseType) -> ProblemTestCase:
    test_case = ProblemTestCase(test_type)

    if test_type is TestCaseType.ZERO:
        N = randint(5, 10)
        f = [0 for _ in range(N)]
        dx = 1

    elif test_type is TestCaseType.CONSTANT:
        N = randint(5, 10)
        c = uniform(-5, 5)
        f = [c for _ in range(N)]
        dx = 1

    elif test_type is TestCaseType.EXPONENTIAL:
        N = randint(20, 40)
        x1, x2 = 0, uniform(3, 5)
        dx = (x2 - x1) / N
        f = [exp(x) for x in linspace(x1, x2, N)]

    test_case.input = {
        "rectangle_heights": f,
        "rectangle_width": dx
    }

    return test_case


def solve_test_case(test_case: ProblemTestCase) -> None:
    f, dx = test_case.input['f'], test_case.input['dx']
    test_case.output['area'] = area_of_rectangles(f, dx)


def verify_user_solution(user_input: tuple, user_output: tuple) -> Tuple[bool, str]:
    user_test_case = ProblemTestCase(None, INPUT_VARS, user_input, OUTPUT_VARS, user_output)
    passed, correct_test_case = test_case_solution_correct(user_test_case, ATOL, RTOL, ProblemTestCase, solve_test_case)
    return passed, correct_test_case.output_str()
