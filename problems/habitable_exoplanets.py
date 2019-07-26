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

PHYSICAL_CONSTANTS = {
    # For the sun L=1 and for the Earth r=1 by definition.
    'L_sun': 1.00,    # [L☉]
    'r_Earth': 1.00,  # [AU]

    # Source: https://en.wikipedia.org/wiki/Proxima_Centauri_b
    'L_Proxima_Centauri': 0.0015,  # [L☉]
    'r_Proxima_Centauri_b': 0.05,  # [AU]

    # Sources:
    # https://en.wikipedia.org/wiki/Kepler-440b (for semi-major axis of 0.242 AU)
    # https://exoplanetarchive.ipac.caltech.edu/cgi-bin/DisplayOverview/nph-DisplayOverview?objname=Kepler-440+b
    #   &type=CONFIRMED_PLANET (for log10(L☉) of -1.102 +0.111 -0.142 => L☉ = 0.079)
    # https://iopscience.iop.org/article/10.1088/0004-637X/800/2/99 (Table 6 for L☉ of 0.079 +0.023 −0.022)
    'L_Kepler_440': 0.079,
    'r_Kepler_440b': 0.242
}

ATOL = {}
RTOL = {}


class TestCaseType(TestCaseTypeEnum):
    EARTH = ("Earth", 1)
    PROXIMA_CENTAURI_B = ("Proxima Centauri b", 1)
    KEPLER_440B = ("Kepler 440b", 1)
    RANDOM = ("Randomly generated exoplanet", 1)


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
        L_star = PHYSICAL_CONSTANTS['L_sun']
        r = PHYSICAL_CONSTANTS['r_Earth']

    elif test_type is TestCaseType.PROXIMA_CENTAURI_B:
        L_star = PHYSICAL_CONSTANTS['L_Proxima_Centauri']
        r = PHYSICAL_CONSTANTS['r_Proxima_Centauri_b']

    elif test_type is TestCaseType.KEPLER_440B:
        L_star = PHYSICAL_CONSTANTS['L_Kepler_440']
        r = PHYSICAL_CONSTANTS['r_Kepler_440b']

    elif test_type is TestCaseType.RANDOM:
        L_star = float(uniform(0.1, 5.0, 1)[0])
        r = float(uniform(0.1, 5.0, 1)[0])

    test_case.input['L_star'] = L_star
    test_case.input['r'] = r
    test_case.output['habitability'] = habitable_exoplanet(L_star, r)

    return test_case


def verify_user_solution(correct_test_case: TestCase, user_input: tuple, user_output: tuple) -> Tuple[bool, str]:
    user_test_case = ProblemTestCase(None, INPUT_VARS, user_input, OUTPUT_VARS, user_output)
    passed, correct_test_case = test_case_solution_correct(correct_test_case, user_test_case, ATOL, RTOL)
    return passed, correct_test_case.output_str()
