import logging
from typing import Tuple

from numpy.random import uniform

from problems.test_case import TestCase, TestCaseTypeEnum
from problems.solutions.rock_star_climate import rock_temperature

logger = logging.getLogger(__name__)

FUNCTION_NAME = "rock_temperature"
INPUT_VARS = ['solar_constant', 'albedo', 'emissivity']
OUTPUT_VARS = ['T_rock']

STATIC_RESOURCES = []

PHYSICAL_CONSTANTS = {
    # Earth
    'S_Earth': 1361,   # Solar constant [W/m^2] from Kopp & Lean (2011).
    'a_Earth': 0.306,  # Bond albedo from NASA Earth fact sheet: https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html
    'ε_Earth': 0.612,  # Effective emissivity.

    # Mars
    'S_Mars': 586,   # Assuming S falls off as 1/r^2 from Kopp & Lean (2011) and r = 1.524 AU.
    'a_Mars': 0.24,  # Bond albedo from NASA Mars fact sheet: https://nssdc.gsfc.nasa.gov/planetary/factsheet/marsfact.html
    'ε_Mars': 0.9,   # Can't find anything so picking a 0.9 which is close to limestone and brick.

    # Pluto
    'S_Pluto': 0.87,  # Assuming S falls off as 1/r^2 from Kopp & Lean (2011) and r = 39.48 AU (semi-major axis).
    'a_Pluto': 0.72,  # Bond albedo from NASA Pluto fact sheet: https://nssdc.gsfc.nasa.gov/planetary/factsheet/plutofact.html
    'ε_Pluto': 0.9
}

ATOL = {}
RTOL = {
    'T_rock': 1e-6
}


class TestCaseType(TestCaseTypeEnum):
    EARTH = ("Earth", 1)
    BLACKBODY_EARTH = ("Blackbody Earth", 1)
    REFLECTIVE_EARTH = ("Reflective Earth", 1)
    MARS = ("Mars", 1)
    PLUTO = ("Pluto", 1)
    RANDOM = ("Random", 1)


class ProblemTestCase(TestCase):
    def input_tuple(self) -> tuple:
        return self.input['solar_constant'], self.input['albedo'], self.input['emissivity'],

    def output_tuple(self) -> tuple:
        return self.output['T_rock'],


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

    elif test_type is TestCaseType.REFLECTIVE_EARTH:
        S = PHYSICAL_CONSTANTS['S_Earth']
        a = 1
        ε = PHYSICAL_CONSTANTS['ε_Earth']

    elif test_type is TestCaseType.MARS:
        S = PHYSICAL_CONSTANTS['S_Mars']
        a = PHYSICAL_CONSTANTS['a_Mars']
        ε = PHYSICAL_CONSTANTS['ε_Mars']

    elif test_type is TestCaseType.PLUTO:
        S = PHYSICAL_CONSTANTS['S_Pluto']
        a = PHYSICAL_CONSTANTS['a_Pluto']
        ε = PHYSICAL_CONSTANTS['ε_Pluto']

    elif test_type is TestCaseType.RANDOM:
        S = uniform(1000, 10000)
        a = uniform(0, 1)
        ε = uniform(0, 1)

    else:
        raise ValueError(f"Unrecognized test case: {test_type}")

    test_case.input = {'solar_constant': S, 'albedo': a, 'emissivity': ε}
    test_case.output['T_rock'] = rock_temperature(S, a, ε)

    return test_case
