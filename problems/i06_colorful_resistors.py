import logging
import numpy as np
from problems.test_case import TestCase, TestCaseTypeEnum

logger = logging.getLogger(__name__)


class TestCaseI6Type(TestCaseTypeEnum):
    ZERO_RESISTOR = ('zero resistor', '', 1)
    FOUR_BAND = ('four band resistor', '', 3)
    FIVE_BAND = ('five band resistor', '', 3)
    UNKNOWN = ('unknown case', '', 0)


class TestCaseI6(TestCase):
    def input_str(self) -> str:
        return ' '.join(self.input['colors'])

    def output_str(self) -> str:
        pass


TEST_CASE_TYPE_ENUM = TestCaseI6Type
TEST_CASE_CLASS = TestCaseI6

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

TESTING_CONSTANTS = {
    'error_tol': 0.1  # tolerance on each resistance output [Ohm]
}


def generate_input(test_type: TestCaseI6Type) -> TestCaseI6:
    digits = PHYSICAL_CONSTANTS['digits']
    multiplier = PHYSICAL_CONSTANTS['multiplier']
    tolerance = PHYSICAL_CONSTANTS['tolerance']

    test_case = TestCaseI6(test_type)

    if test_type is TestCaseI6Type.ZERO_RESISTOR:
        colors = ['black']
    elif test_type is TestCaseI6Type.FOUR_BAND:
        band_color1 = np.random.choice(list(digits.keys()))
        band_color2 = np.random.choice(list(digits.keys()))
        multiplier_color = np.random.choice(list(multiplier.keys()))
        tolerance_color = np.random.choice(list(tolerance.keys()))
        colors = [band_color1, band_color2, multiplier_color, tolerance_color]
    elif test_type is TestCaseI6Type.FIVE_BAND:
        band_color1 = np.random.choice(list(digits.keys()))
        band_color2 = np.random.choice(list(digits.keys()))
        band_color3 = np.random.choice(list(digits.keys()))
        multiplier_color = np.random.choice(list(multiplier.keys()))
        tolerance_color = np.random.choice(list(tolerance.keys()))
        colors = [band_color1, band_color2, band_color3, multiplier_color, tolerance_color]

    test_case.input['colors'] = colors
    return test_case


def solve_test_case(test_case: TestCaseI6) -> None:
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
    logger.info("Verifying user solution...")
    logger.debug("User input string: %s", user_input_str)
    logger.debug("User output string: %s", user_output_str)

    # Build TestCase object out of user's input string.
    tmp_test_case = TestCaseI6(TestCaseI6Type.UNKNOWN)

    inputs = user_input_str.split()
    colors = inputs
    tmp_test_case.input = {'colors': colors}

    # Solve the problem with this TestCase so we have our own solution, and extract the solution.
    solve_test_case(tmp_test_case)
    nominal_R = tmp_test_case.output['nominal_resistance']
    minimum_R = tmp_test_case.output['minimum_resistance']
    maximum_R = tmp_test_case.output['maximum_resistance']

    # Extract user solution.
    outputs = list(map(float, user_output_str.split()))
    user_nominal_R = outputs[0]
    user_minimum_R = outputs[1]
    user_maximum_R = outputs[2]

    error_tol = TESTING_CONSTANTS['error_tol']
    error_R = abs(nominal_R - user_nominal_R) + abs(minimum_R - user_minimum_R) + abs(maximum_R - user_maximum_R)

    logger.debug("User solution:")
    logger.debug("nominal_R = %f, minimum_R = %f, maximum_R = %f", user_nominal_R, user_minimum_R, user_maximum_R)
    logger.debug("Engine solution:")
    logger.debug("nominal_R = %f, minimum_R = %f, maximum_R = %f", nominal_R, minimum_R, maximum_R)
    logger.debug("Error tolerance = %e. Error x: %e.", error_tol, error_R)

    if error_R < error_tol:
        logger.info("User solution correct.")
        return True
    else:
        logger.info("User solution incorrect.")
        return False
