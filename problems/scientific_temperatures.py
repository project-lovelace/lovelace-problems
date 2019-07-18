import logging
from typing import Tuple
from numpy.random import uniform

from problems.test_case import TestCase, TestCaseTypeEnum, test_case_solution_correct

logger = logging.getLogger(__name__)

FUNCTION_NAME = "fahrenheit_to_celsius"
INPUT_VARS = ['F']
OUTPUT_VARS = ['C']

STATIC_RESOURCES = []

PHYSICAL_CONSTANTS = {}
ATOL = {}
RTOL = {
    'C': 1e-5
}


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
        return self.input['F'],

    def output_tuple(self) -> tuple:
        return self.output['C'],

    def output_str(self) -> str:
        return str(self.output['C'])


def generate_test_case(test_type: TestCaseType) -> ProblemTestCase:
    test_case = ProblemTestCase(test_type)

    if test_type is TestCaseType.WARM_DAY:
        F = uniform(80, 110)

    elif test_type is TestCaseType.COLD_DAY:
        F = uniform(-20, 30)

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

    test_case.input['F'] = F
    return test_case


def solve_test_case(test_case: ProblemTestCase) -> None:
    F = test_case.input['F']
    test_case.output['C'] = (5/9) * (F - 32)


def verify_user_solution(user_input: tuple, user_output: tuple) -> Tuple[bool, str]:
    user_test_case = ProblemTestCase(None, INPUT_VARS, user_input, OUTPUT_VARS, user_output)
    passed, correct_test_case = test_case_solution_correct(user_test_case, ATOL, RTOL, ProblemTestCase, solve_test_case)
    return passed, correct_test_case.output_str()
