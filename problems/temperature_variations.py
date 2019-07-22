import logging
from typing import Tuple
from numpy.random import randint, uniform

from problems.test_case import TestCase, TestCaseTypeEnum, test_case_solution_correct
from problems.solutions.temperature_variations import temperature_statistics

logger = logging.getLogger(__name__)

FUNCTION_NAME = "temperature_statistics"
INPUT_VARS = ['T']
OUTPUT_VARS = ['T_avg', 'T_std']

STATIC_RESOURCES = []

PHYSICAL_CONSTANTS = {
    'T': {
        'Saskatoon, Canada': [-13.9, -11.4, -4.9, 5.2, 11.8, 16.1, 19.0, 18.2, 12.0, 4.4, -5.2, -12.4],
        'Baku, Azerbaijan': [4.4, 4.2, 7.0, 12.9, 18.5, 23.5, 26.4, 26.3, 22.5, 16.6, 11.2, 7.3],
        'Khartoum, Sudan': [23.2, 25.0, 28.7, 31.9, 34.5, 34.3, 32.1, 31.5, 32.5, 32.4, 28.1, 24.5],
        'Singapore': [26.5, 27.1, 27.5, 28.0, 28.3, 28.3, 27.9, 27.9, 27.6, 27.6, 27.0, 26.4],
        'San Juan, Argentina': [27.1, 25.5, 22.8, 17.2, 12.2, 8.3, 7.7, 10.6, 14.4, 19.8, 23.4, 26.3]
    }
}

ATOL = {}
RTOL = {
    'T_avg': 1e-8,
    'T_std': 1e-8
}


class TestCaseType(TestCaseTypeEnum):
    ONE_VALUE = ("One value", 1)
    TWO_VALUES = ("Two values", 1)
    BUNCH_OF_VALUES = ("Bunch of values", 1)
    SASKATOON = ("Saskatoon, Canada", 1)
    BAKU = ("Baku, Azerbaijan", 1)
    KHARTOUM = ("Khartoum, Sudan", 1)
    SINGAPORE = ("Singapore", 1)
    SAN_JUAN = ("San Juan, Argentina", 1)


class ProblemTestCase(TestCase):
    def input_tuple(self) -> tuple:
        return self.input['T'],

    def output_tuple(self) -> tuple:
        return self.output['T_avg'], self.output['T_std']

    def output_str(self) -> str:
        return "T_avg = {:.4f}, T_std = {:.4f}".format(self.output['T_avg'], self.output['T_std'])


def generate_test_case(test_type: TestCaseType) -> ProblemTestCase:
    test_case = ProblemTestCase(test_type)

    if test_type is TestCaseType.ONE_VALUE:
        T = [uniform(-20, 35)]

    elif test_type is TestCaseType.TWO_VALUES:
        T = uniform(-20, 35, size=2).tolist()

    elif test_type is TestCaseType.BUNCH_OF_VALUES:
        N = randint(5, 20)
        T = uniform(-20, 35, size=N).tolist()

    elif test_type is TestCaseType.SASKATOON:
        T = PHYSICAL_CONSTANTS['T']['Saskatoon, Canada']

    elif test_type is TestCaseType.BAKU:
        T = PHYSICAL_CONSTANTS['T']['Baku, Azerbaijan']

    elif test_type is TestCaseType.KHARTOUM:
        T = PHYSICAL_CONSTANTS['T']['Khartoum, Sudan']

    elif test_type is TestCaseType.SINGAPORE:
        T = PHYSICAL_CONSTANTS['T']['Singapore']

    elif test_type is TestCaseType.SAN_JUAN:
        T = PHYSICAL_CONSTANTS['T']['San Juan, Argentina']

    test_case.input['T'] = T
    return test_case


def solve_test_case(test_case: ProblemTestCase) -> None:
    T = test_case.input['T']
    test_case.output['T_avg'], test_case.output['T_std'] = temperature_statistics(T)


def verify_user_solution(user_input: tuple, user_output: tuple) -> Tuple[bool, str]:
    user_test_case = ProblemTestCase(None, INPUT_VARS, user_input, OUTPUT_VARS, user_output)
    passed, correct_test_case = test_case_solution_correct(user_test_case, ATOL, RTOL, ProblemTestCase, solve_test_case)
    return passed, correct_test_case.output_str()
