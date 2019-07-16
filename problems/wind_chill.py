import logging
from typing import Tuple
from numpy.random import uniform

from problems.test_case import TestCase, TestCaseTypeEnum, test_case_solution_correct
from problems.solutions.wind_chill import wind_chill

logger = logging.getLogger(__name__)


class TestCaseType(TestCaseTypeEnum):
    COLD_CALM = ("Cold calm weather", 1)
    COLD_WINDY = ("Cold windy weather", 1)
    VERY_COLD_CALM = ("Very cold and calm weather", 1)
    VERY_COLD_WINDY = ("Very cold and windy weather", 1)


class ProblemTestCase(TestCase):
    def input_tuple(self) -> tuple:
        return self.input['T_a'], self.input['v']

    def output_tuple(self) -> tuple:
        return self.output['T_wc'],

    def output_str(self) -> str:
        return str(self.output['T_wc'])


FUNCTION_NAME = "wind_chill"
STATIC_RESOURCES = []

INPUT_VARS = ['T_a', 'v']
OUTPUT_VARS = ['T_wc']

PHYSICAL_CONSTANTS = {}
ATOL = {}
RTOL = {
    'T_wc': 1e-8
}


def generate_test_case(test_type: TestCaseType) -> ProblemTestCase:
    test_case = ProblemTestCase(test_type)

    if test_type is TestCaseType.COLD_CALM:
        T_a = uniform(-15, 2)
        v = uniform(2, 8)

    elif test_type is TestCaseType.COLD_WINDY:
        T_a = uniform(-15, 2)
        v = uniform(25, 60)

    elif test_type is TestCaseType.VERY_COLD_CALM:
        T_a = uniform(-50, -20)
        v = uniform(2, 8)

    elif test_type is TestCaseType.VERY_COLD_WINDY:
        T_a = uniform(-50, -20)
        v = uniform(25, 60)

    test_case.input['T_a'], test_case.input['v'] = T_a, v
    return test_case


def solve_test_case(test_case: ProblemTestCase) -> None:
    T_a = test_case.input['T_a']
    v = test_case.input['v']
    test_case.output['T_wc'] = wind_chill(T_a, v)


def verify_user_solution(user_input: tuple, user_output: tuple) -> Tuple[bool, str]:
    user_test_case = ProblemTestCase(None, INPUT_VARS, user_input, OUTPUT_VARS, user_output)
    passed, correct_test_case = test_case_solution_correct(user_test_case, ATOL, RTOL, ProblemTestCase, solve_test_case)
    return passed, correct_test_case.output_str()
