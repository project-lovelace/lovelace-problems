import logging

import numpy as np

from problems.test_case import TestCase, TestCaseTypeEnum

logger = logging.getLogger(__name__)


class TestCase6Type(TestCaseTypeEnum):
    ZERO_RESISTOR = ('zero resistor', 1)
    FOUR_BAND = ('four band resistor', 3)
    FIVE_BAND = ('five band resistor', 3)


class TestCase6(TestCase):
    def input_tuple(self) -> str:
        return (self.input['colors'],)

    def output_tuple(self) -> str:
        nominal_R = tmp_test_case.output['nominal_resistance']
        minimum_R = tmp_test_case.output['minimum_resistance']
        maximum_R = tmp_test_case.output['maximum_resistance']
        return (nominal_R, minimum_R, maximum_R)


TEST_CASE_TYPE_ENUM = TestCase6Type
TEST_CASE_CLASS = TestCase6
FUNCTION_NAME = "resistance"
STATIC_RESOURCES = []

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


def generate_test_case(test_type: TestCase6Type) -> TestCase6:
    digits = PHYSICAL_CONSTANTS['digits']
    multiplier = PHYSICAL_CONSTANTS['multiplier']
    tolerance = PHYSICAL_CONSTANTS['tolerance']

    test_case = TestCase6(test_type)

    # We have the str() of each random choice as np.random.choice()
    # returns an np.str_ object and the test cases will fail if the user
    # hasn't imported numpy.
    if test_type is TestCase6Type.ZERO_RESISTOR:
        colors = ['black']
    elif test_type is TestCase6Type.FOUR_BAND:
        band_color1 = str(np.random.choice(list(digits.keys())))
        band_color2 = str(np.random.choice(list(digits.keys())))
        multiplier_color = str(np.random.choice(list(multiplier.keys())))
        tolerance_color = str(np.random.choice(list(tolerance.keys())))
        colors = [band_color1, band_color2, multiplier_color, tolerance_color]
    elif test_type is TestCase6Type.FIVE_BAND:
        band_color1 = str(np.random.choice(list(digits.keys())))
        band_color2 = str(np.random.choice(list(digits.keys())))
        band_color3 = str(np.random.choice(list(digits.keys())))
        multiplier_color = str(np.random.choice(list(multiplier.keys())))
        tolerance_color = str(np.random.choice(list(tolerance.keys())))
        colors = [band_color1, band_color2, band_color3, multiplier_color, tolerance_color]

    test_case.input['colors'] = colors
    return test_case


def solve_test_case(test_case: TestCase6) -> None:
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


def verify_user_solution(user_input: tuple, user_output: tuple) -> bool:
    logger.info("Verifying user solution...")
    logger.debug("User input: %s", user_input)
    logger.debug("User output: %s", user_output)

    # Build TestCase object out of user's input string.
    tmp_test_case = TestCase6()

    colors = user_input[0]
    tmp_test_case.input = {'colors': colors}

    # Solve the problem with this TestCase so we have our own solution, and extract the solution.
    solve_test_case(tmp_test_case)
    nominal_R = tmp_test_case.output['nominal_resistance']
    minimum_R = tmp_test_case.output['minimum_resistance']
    maximum_R = tmp_test_case.output['maximum_resistance']

    # Extract user solution.
    user_nominal_R, user_minimum_R, user_maximum_R = user_output

    error_tol = TESTING_CONSTANTS['error_tol']
    error_R = abs(nominal_R - user_nominal_R) + abs(minimum_R - user_minimum_R) + abs(maximum_R - user_maximum_R)

    logger.debug("User solution:")
    logger.debug("nominal_R = %f, minimum_R = %f, maximum_R = %f", user_nominal_R, user_minimum_R, user_maximum_R)
    logger.debug("Engine solution:")
    logger.debug("nominal_R = %f, minimum_R = %f, maximum_R = %f", nominal_R, minimum_R, maximum_R)
    logger.debug("Error tolerance = %e. Error x: %e.", error_tol, error_R)

    passed = False

    if error_R < error_tol:
        logger.info("User solution correct within error tolerance of {:g}.".format(error_tol))
        passed = True
    else:
        logger.info("User solution incorrect.")

    return passed, "nominal_R = {}, minimum_R = {}, maximum_R = {}".format(nominal_R, minimum_R, maximum_R)
