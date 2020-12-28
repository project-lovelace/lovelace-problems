import logging
from typing import Tuple
from numpy.random import uniform

from problems.test_case import TestCase, TestCaseTypeEnum
from problems.solutions.wind_chill import wind_chill

logger = logging.getLogger(__name__)

FUNCTION_NAME = "wind_chill"
INPUT_VARS = ['T_a', 'v']
OUTPUT_VARS = ['T_wc']

STATIC_RESOURCES = []

PHYSICAL_CONSTANTS = {}
ATOL = {}
RTOL = {
    'T_wc': 1e-8
}


class TestCaseType(TestCaseTypeEnum):
    ZERO_TEMP = ("Zero celsius", 1)
    ZERO_WIND = ("Zero wind", 1)
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


def generate_test_case(test_type: TestCaseType) -> ProblemTestCase:
    test_case = ProblemTestCase(test_type)

    if test_type is TestCaseType.ZERO_TEMP:
        T_a = 0
        v = uniform(5, 40)

    if test_type is TestCaseType.ZERO_WIND:
        T_a = uniform(-20, 20)
        v = 0

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
    test_case.output['T_wc'] = wind_chill(T_a, v)

    return test_case
