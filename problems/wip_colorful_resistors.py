import numpy as np

from problems.test_case import TestCase, TestCaseTypeEnum

from os import path
import logging, logging.config

logging_config_path = path.join(path.dirname(path.abspath(__file__)), '..', 'logging.ini')
logging.config.fileConfig(logging_config_path)
logger = logging.getLogger(__name__)


class TestCase8Type(TestCaseTypeEnum):
    ZERO_RESISTOR = ('zero resistor', '', 1)
    FOUR_BAND = ('four band resistor', '', 3)
    FIVE_BAND = ('five band resistor', '', 3)


class TestCase8(TestCase):
    def input_str(self) -> str:
        return ' '.join(self.input['colors'])

    def output_str(self) -> str:
        pass


TEST_CASE_TYPE_ENUM = TestCase8Type
TEST_CASE_CLASS = TestCase8

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
TESTING_CONSTANTS = {}


def generate_input(test_type: TestCase8Type) -> TestCase8:
    digits = PHYSICAL_CONSTANTS['digits']
    multiplier = PHYSICAL_CONSTANTS['multiplier']
    tolerance = PHYSICAL_CONSTANTS['tolerance']

    test_case = TestCase8(test_type)

    if test_type is TestCase8Type.ZERO_RESISTOR:
        colors = ['black']
    elif test_type is TestCase8Type.FOUR_BAND:
        band_color1 = np.random.choice(digits.keys())
        band_color2 = np.random.choice(digits.keys())
        multiplier_color = np.random.choice(multiplier.keys())
        tolerance_color = np.random.choice(tolerance.keys())
        colors = [band_color1, band_color2, multiplier_color, tolerance_color]
    elif test_type is TestCase8Type.FIVE_BAND:
        band_color1 = np.random.choice(digits.keys())
        band_color2 = np.random.choice(digits.keys())
        band_color3 = np.random.choice(digits.keys())
        multiplier_color = np.random.choice(multiplier.keys())
        tolerance_color = np.random.choice(tolerance.keys())
        colors = [band_color1, band_color2, band_color3, multiplier_color, tolerance_color]

    test_case.input['colors'] = colors
    return test_case


def solve_test_case(test_case: TestCase8) -> None:
    digits = PHYSICAL_CONSTANTS['digits']
    multiplier = PHYSICAL_CONSTANTS['multiplier']
    tolerance = PHYSICAL_CONSTANTS['tolerance']
    
    colors = test_case.input['colors']
    n_bands = len(colors)
    
    if n_bands == 1 and colors[0] == 'black':
        nominal_R = 0
        minimum_R = 0
        maximum_R = 0
    elif n_bands == 4:
        nominal_R = 10*digits[colors[0]] + digits[colors[1]]
        nominal_R *= multiplier[colors[2]]
        minimum_R = (1 - tolerance[colors[3]]) * nominal_R
        maximum_R = (1 + tolerance[colors[3]]) * nominal_R
    elif n_bands == 5:
        nominal_R = 100*digits[colors[0]] + 10 * digits[colors[1]] + digits[colors[2]]
        nominal_R *= multiplier[colors[3]]
        minimum_R = (1 - tolerance[colors[4]]) * nominal_R
        maximum_R = (1 + tolerance[colors[4]]) * nominal_R

    test_case.output['nominal_resistance'] = nominal_R
    test_case.output['minimum_resistance'] = minimum_R
    test_case.output['maximum_resistance'] = maximum_R
    return


def verify_user_solution(user_input_str: str, user_output_str: str) -> bool:
    pass
