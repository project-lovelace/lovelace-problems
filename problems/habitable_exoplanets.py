import logging
from typing import Tuple

from numpy.random import uniform

from problems.test_case import TestCase, TestCaseTypeEnum, test_case_solution_correct
from problems.solutions.habitable_exoplanets import habitable_exoplanet

logger = logging.getLogger(__name__)

FUNCTION_NAME = "habitable_exoplanet"
INPUT_VARS = ['L_star', 'r']
OUTPUT_VARS = ['habitability']

STATIC_RESOURCES = []

PHYSICAL_CONSTANTS = {}
ATOL = {}
RTOL = {}


class TestCaseType(TestCaseTypeEnum):
    EARTH = ('Earth', 1)
    PROXIMA_CENTAURI_B = ('Proxima Centauri b', 1)
    KEPLER_440B = ('Kepler 440b', 1)
    RANDOM = ('Randomly generated exoplanet', 1)


class ProblemTestCase(TestCase):
    def input_tuple(self) -> tuple:
        return self.input['L_star'], self.input['r']

    def output_tuple(self) -> tuple:
        return self.output['habitability'],

    def output_str(self) -> str:
        return str(self.output['habitability'])


def generate_test_case(test_type: TestCaseType) -> ProblemTestCase:
    test_case = ProblemTestCase(test_type)

    if test_type is TestCaseType.EARTH:
        L_star = 1.00
        r = 1.00
    elif test_type is TestCaseType.PROXIMA_CENTAURI_B:
        L_star = 1.00
        r = 1.00
    elif test_type is TestCaseType.KEPLER_440B:
        L_star = 1.43
        r = 0.242
    elif test_type is TestCaseType.RANDOM:
        L_star = float(uniform(0.1, 5.0, 1)[0])
        r = float(uniform(0.1, 5.0, 1)[0])

    test_case.input['L_star'] = L_star
    test_case.input['r'] = r
    return test_case


def solve_test_case(test_case: ProblemTestCase) -> None:
    L_star = test_case.input['L_star']
    r = test_case.input['r']
    test_case.output['habitability'] = habitable_exoplanet(L_star, r)


def verify_user_solution(user_input: tuple, user_output: tuple) -> Tuple[bool, str]:
    user_test_case = ProblemTestCase(None, INPUT_VARS, user_input, OUTPUT_VARS, user_output)
    passed, correct_test_case = test_case_solution_correct(user_test_case, ATOL, RTOL, ProblemTestCase, solve_test_case)
    return passed, correct_test_case.output_str()
