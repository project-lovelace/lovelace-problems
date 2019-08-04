import logging
from typing import Tuple
from numpy import pi, exp, sin, linspace, ndarray
from numpy.random import randint, uniform

from problems.test_case import TestCase, TestCaseTypeEnum, test_case_solution_correct
from problems.solutions.definite_integrals import area_of_rectangles

logger = logging.getLogger(__name__)

FUNCTION_NAME = "area_of_rectangles"
INPUT_VARS = ['rectangle_heights', 'rectangle_width']
OUTPUT_VARS = ['area']

STATIC_RESOURCES = []

PHYSICAL_CONSTANTS = {}
ATOL = {
    'area': 1e-6
}
RTOL = {}


class TestCaseType(TestCaseTypeEnum):
    ZERO = ("Zero function (rectangles with no height)", 1)
    CONSTANT = ("Constant function (all rectangles have the same height)", 1)
    LINEAR = ("Linear function", 1)
    QUADRATIC = ("Quadratic polynomial", 1)
    EXPONENTIAL = ("Exponential function", 1)
    SINE = ("Sine function", 1)
    RANDOM = ("Random function", 1)


class ProblemTestCase(TestCase):
    def input_tuple(self) -> tuple:
        return self.input['rectangle_heights'], self.input['rectangle_width']

    def output_tuple(self) -> tuple:
        return self.output['area'],

    def output_str(self) -> str:
        return str(self.output['area'])


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

    elif test_type is TestCaseType.LINEAR:
        N = randint(10, 20)
        x1, x2 = uniform(0, 2), uniform(3, 5)
        dx = (x2 - x1) / N

        a, b = uniform(-5, 5), uniform(-5, 5)
        f = [a*x + b for x in linspace(x1, x2, N)]

    elif test_type is TestCaseType.QUADRATIC:
        N = randint(15, 30)
        x1, x2 = uniform(-5, -1), uniform(2, 5)
        dx = (x2 - x1) / N

        a, b, c = uniform(-1, 1), uniform(-1, 1), uniform(-1, 1)
        f = [a*x**2 + b*x + c for x in linspace(x1, x2, N)]

    elif test_type is TestCaseType.EXPONENTIAL:
        N = randint(20, 40)
        x1, x2 = 0, uniform(3, 5)
        dx = (x2 - x1) / N
        f = [exp(x) for x in linspace(x1, x2, N)]

    elif test_type is TestCaseType.SINE:
        N = randint(50, 75)
        x1, x2 = 0, 2*pi
        dx = (x2 - x1) / N
        f = [sin(x) for x in linspace(x1, x2, N)]

    elif test_type is TestCaseType.RANDOM:
        N = randint(40, 60)
        x1, x2 = 0, 1
        dx = (x2 - x1) / N
        f = uniform(-1, 1, size=N)

    test_case.input = {
        "rectangle_heights": f.tolist() if isinstance(f, ndarray) else f,
        "rectangle_width": float(dx)
    }

    test_case.output['area'] = float(area_of_rectangles(f, dx))

    return test_case


def verify_user_solution(correct_test_case: TestCase, user_input: tuple, user_output: tuple) -> Tuple[bool, str]:
    user_test_case = ProblemTestCase(None, INPUT_VARS, user_input, OUTPUT_VARS, user_output)
    passed, correct_test_case = test_case_solution_correct(correct_test_case, user_test_case, ATOL, RTOL)
    return passed, correct_test_case.output_str()
