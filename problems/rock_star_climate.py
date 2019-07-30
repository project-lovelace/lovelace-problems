import logging
from typing import Tuple

from numpy.random import uniform

from problems.test_case import TestCase, TestCaseTypeEnum, test_case_solution_correct
from problems.solutions.rock_star_climate import rock_temperature

logger = logging.getLogger(__name__)

FUNCTION_NAME = "rock_temperature"
INPUT_VARS = ['solar_constant', 'albedo', 'emissivity']
OUTPUT_VARS = ['T_rock']

STATIC_RESOURCES = []

PHYSICAL_CONSTANTS = {
    # Earth
    'S_Earth': 1361,  # Solar constant [W/m^2] from Kopp & Lean (2011).
    'a_Earth': 0.306,  # Bond albedo from NASA Earth fact sheet.
    'ε_Earth': 0.612  # Effective emissivity.
}

ATOL = {}
RTOL = {
    'T_rock': 1e-6
}


class TestCaseType(TestCaseTypeEnum):
    EARTH = ("Earth", 1)
    BLACKBODY_EARTH = ("Blackbody Earth", 1)


class ProblemTestCase(TestCase):
    def input_tuple(self) -> tuple:
        return self.input['solar_constant'], self.input['albedo'], self.input['emissivity'],

    def output_tuple(self) -> tuple:
        return self.output['T_rock'],

    def output_str(self) -> str:
        return str(self.output['T_rock'])


def generate_test_case(test_type: TestCaseType) -> ProblemTestCase:
    test_case = ProblemTestCase(test_type)

    if test_type is TestCaseType.EARTH:
        S = PHYSICAL_CONSTANTS['S_Earth']
        a = PHYSICAL_CONSTANTS['a_Earth']
        ε = PHYSICAL_CONSTANTS['ε_Earth']

    elif test_type is TestCaseType.BLACKBODY_EARTH:
        S = PHYSICAL_CONSTANTS['S_Earth']
        a = PHYSICAL_CONSTANTS['a_Earth']
        ε = 1.0

    test_case.input = {'solar_constant': S, 'albedo': a, 'emissivity': ε}
    test_case.output['T_rock'] = rock_temperature(S, a, ε)

    return test_case


def verify_user_solution(correct_test_case: TestCase, user_input: tuple, user_output: tuple) -> Tuple[bool, str]:
    user_test_case = ProblemTestCase(None, INPUT_VARS, user_input, OUTPUT_VARS, user_output)
    passed, correct_test_case = test_case_solution_correct(correct_test_case, user_test_case, ATOL, RTOL)
    return passed, correct_test_case.output_str()
