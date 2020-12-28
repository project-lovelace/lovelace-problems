import logging
from typing import Tuple

from numpy.random import uniform

from problems.test_case import TestCase, TestCaseTypeEnum
from problems.solutions.rocket_science import rocket_fuel

logger = logging.getLogger(__name__)

FUNCTION_NAME = "rocket_fuel"
INPUT_VARS = ['v']
OUTPUT_VARS = ['m_fuel']

STATIC_RESOURCES = []

PHYSICAL_CONSTANTS = {
    'v_e': 2550.0,  # [m/s]
    'M': 250000.0,  # [kg]

    # All escape velocities in [m/s].
    # Source: https://en.wikipedia.org/wiki/Escape_velocity#List_of_escape_velocities
    'v_Earth': 11186.0,
    'v_Moon': 2380.0,
    'v_Jupiter': 60200.0,
    'v_Pluto': 1230.0,
    'v_Phobos': 1.139
}

ATOL = {}
RTOL = {
    'm_fuel': 1e-6
}


class TestCaseType(TestCaseTypeEnum):
    EARTH = ('Earth', 1)
    MOON = ('Moon', 1)
    JUPITER = ('Jupiter', 1)
    PLUTO = ('Pluto', 1)
    PHOBOS = ('Phobos', 1)
    RANDOM = ('Random', 1)


class ProblemTestCase(TestCase):
    def input_tuple(self) -> tuple:
        return self.input['v'],

    def output_tuple(self) -> tuple:
        return self.output['m_fuel'],

    def output_str(self) -> str:
        return str(self.output['m_fuel'])


def generate_test_case(test_type: TestCaseType) -> ProblemTestCase:
    test_case = ProblemTestCase(test_type)

    if test_type is TestCaseType.EARTH:
        v = PHYSICAL_CONSTANTS['v_Earth']

    elif test_type is TestCaseType.MOON:
        v = PHYSICAL_CONSTANTS['v_Moon']

    elif test_type is TestCaseType.JUPITER:
        v = PHYSICAL_CONSTANTS['v_Jupiter']

    elif test_type is TestCaseType.PLUTO:
        v = PHYSICAL_CONSTANTS['v_Pluto']

    elif test_type is TestCaseType.PHOBOS:
        v = PHYSICAL_CONSTANTS['v_Phobos']

    elif test_type is TestCaseType.RANDOM:
        v = float(uniform(1.0, 100.0, 1)[0])

    test_case.input['v'] = v
    test_case.output['m_fuel'] = rocket_fuel(v)

    return test_case
