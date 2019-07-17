import logging
from typing import Tuple
from numpy import mean, var
from numpy.random import randint, uniform

from problems.test_case import TestCase, TestCaseTypeEnum, test_case_solution_correct

logger = logging.getLogger(__name__)

FUNCTION_NAME = "temperature_statistics"
INPUT_VARS = ['temperatures']
OUTPUT_VARS = ['T_avg', 'T_var']

STATIC_RESOURCES = []

PHYSICAL_CONSTANTS = {}
ATOL = {}
RTOL = {
    'T_avg': 1e-8,
    'T_var': 1e-8
}

class TestCaseType(TestCaseTypeEnum):
    RANDOM_SMALL = ("Random (small)", 1)
    RANDOM_LARGE = ("Random (large)", 1)


class ProblemTestCase(TestCase):
    def input_tuple(self) -> tuple:
        return self.input['temperatures'],

    def output_tuple(self) -> tuple:
        return self.output['T_avg'], self.output['T_var']


def generate_test_case(test_type: TestCaseType) -> ProblemTestCase:
    test_case = ProblemTestCase(test_type)

    if test_type is TestCaseType.RANDOM_SMALL:
        n = randint(5, 15)
        Ts = uniform(-20, 35, size=n)

    elif test_type is TestCaseType.SUN_TO_EARTH:
        n = randint(1000, 2000)
        Ts = uniform(-20, 35, size=n)

    test_case.input["temperatures"] = Ts
    return test_case


def solve_test_case(test_case: ProblemTestCase) -> None:
    T = test_case.input['temperatures']
    test_case.output['T_avg'] = mean(T)
    test_case.output['T_var'] = var(T)


def verify_user_solution(user_input: tuple, user_output: tuple) -> Tuple[bool, str]:
    user_test_case = ProblemTestCase(None, INPUT_VARS, user_input, OUTPUT_VARS, user_output)
    passed, correct_test_case = test_case_solution_correct(user_test_case, ATOL, RTOL, ProblemTestCase, solve_test_case)
    return passed, correct_test_case.output_str()
