import logging
from typing import Tuple

import numpy as np

from problems.test_case import TestCase, TestCaseTypeEnum, test_case_solution_correct
from problems.solutions.colorful_resistors import resistance

logger = logging.getLogger(__name__)

FUNCTION_NAME = "resistance"
STATIC_RESOURCES = []

INPUT_VARS = ['colors']
OUTPUT_VARS = ['nominal_resistance', 'minimum_resistance', 'maximum_resistance']

PHYSICAL_CONSTANTS = {
    'digits': {
        'black': 0,
        'brown': 1,
        'red': 2,
        'orange': 3,
        'yellow': 4,
        'green': 5,
        'blue': 6,
        'violet': 7,
        'grey': 8,
        'white': 9
    },
    'multiplier': {
        'pink': 0.001,
        'silver': 0.01,
        'gold': 0.1,
        'black': 1,
        'brown': 10,
        'red': 100,
        'orange': 10**3,
        'yellow': 10**4,
        'green': 10**5,
        'blue': 10**6,
        'violet': 10**7,
        'grey': 10**8,
        'white': 10**9
    },
    'tolerance': {
        'none': 0.2,
        'silver': 0.1,
        'gold': 0.05,
        'brown': 0.01,
        'red': 0.02,
        'green': 0.005,
        'blue': 0.0025,
        'violet': 0.001,
        'grey': 0.0005
    }
}

ATOL = {}
RTOL = {
    'nominal_resistance': 1e-6,
    'minimum_resistance': 1e-6,
    'maximum_resistance': 1e-6
}


class TestCaseType(TestCaseTypeEnum):
    ZERO_RESISTOR = ('zero resistor', 1)
    FOUR_BAND = ('four band resistor', 3)
    FIVE_BAND = ('five band resistor', 3)


class ProblemTestCase(TestCase):
    def input_tuple(self) -> tuple:
        return self.input['colors'],

    def output_tuple(self) -> tuple:
        nominal_R = self.output['nominal_resistance']
        minimum_R = self.output['minimum_resistance']
        maximum_R = self.output['maximum_resistance']
        return nominal_R, minimum_R, maximum_R

    def output_str(self) -> str:
        nominal_R = self.output['nominal_resistance']
        minimum_R = self.output['minimum_resistance']
        maximum_R = self.output['maximum_resistance']
        return "nominal_R = {:f}, minimum_R = {:f}, maximum_R = {:f}".format(nominal_R, minimum_R, maximum_R)


def generate_test_case(test_type: TestCaseType) -> ProblemTestCase:
    digits = PHYSICAL_CONSTANTS['digits']
    multiplier = PHYSICAL_CONSTANTS['multiplier']
    tolerance = PHYSICAL_CONSTANTS['tolerance']

    test_case = ProblemTestCase(test_type)

    # We use the str() of each random choice as np.random.choice()
    # returns an np.str_ object and the test cases will fail if the user
    # hasn't imported numpy: we want a string, not an np.str_!
    if test_type is TestCaseType.ZERO_RESISTOR:
        colors = ['black']

    elif test_type is TestCaseType.FOUR_BAND:
        band_color1 = str(np.random.choice(list(digits.keys())))
        band_color2 = str(np.random.choice(list(digits.keys())))
        multiplier_color = str(np.random.choice(list(multiplier.keys())))
        tolerance_color = str(np.random.choice(list(tolerance.keys())))
        colors = [band_color1, band_color2, multiplier_color, tolerance_color]

    elif test_type is TestCaseType.FIVE_BAND:
        band_color1 = str(np.random.choice(list(digits.keys())))
        band_color2 = str(np.random.choice(list(digits.keys())))
        band_color3 = str(np.random.choice(list(digits.keys())))
        multiplier_color = str(np.random.choice(list(multiplier.keys())))
        tolerance_color = str(np.random.choice(list(tolerance.keys())))
        colors = [band_color1, band_color2, band_color3, multiplier_color, tolerance_color]

    test_case.input['colors'] = colors

    nominal_R, minimum_R, maximum_R = resistance(colors)
    test_case.output['nominal_resistance'] = nominal_R
    test_case.output['minimum_resistance'] = minimum_R
    test_case.output['maximum_resistance'] = maximum_R

    return test_case


def verify_user_solution(correct_test_case: TestCase, user_input: tuple, user_output: tuple) -> Tuple[bool, str]:
    user_test_case = ProblemTestCase(None, INPUT_VARS, user_input, OUTPUT_VARS, user_output)
    passed, correct_test_case = test_case_solution_correct(correct_test_case, user_test_case, ATOL, RTOL)
    return passed, correct_test_case.output_str()
