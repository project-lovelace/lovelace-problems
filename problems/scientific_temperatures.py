import logging
from typing import Tuple
from numpy.random import uniform

from problems.test_case import TestCase, TestCaseTypeEnum
from problems.solutions.scientific_temperatures import fahrenheit_to_celsius

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


def generate_test_case(test_type: TestCaseType) -> ProblemTestCase:
    test_case = ProblemTestCase(test_type)

    if test_type is TestCaseType.WARM_DAY:
        F = uniform(80, 110)

    elif test_type is TestCaseType.COLD_DAY:
        F = uniform(-20, 30)

    elif test_type is TestCaseType.WATER_FREEZING_POINT:
        F = 32.0

    elif test_type is TestCaseType.WATER_BOILING_POINT:
        F = 212.0

    elif test_type is TestCaseType.MINUS_40:
        F = -40.0

    elif test_type is TestCaseType.ABSOLUTE_ZERO:
        F = -459.67

    elif test_type is TestCaseType.SUN_SURFACE:
        F = 9940.73

    else:
        raise ValueError(f"Unrecognized test case: {test_type}")

    test_case.input['F'] = F
    test_case.output['C'] = fahrenheit_to_celsius(F)
    return test_case
