import logging
from typing import Tuple
from numpy.random import uniform

from problems.test_case import TestCase, TestCaseTypeEnum
from problems.solutions.speed_of_light import light_time

logger = logging.getLogger(__name__)

FUNCTION_NAME = "light_time"
INPUT_VARS = ['distance']
OUTPUT_VARS = ['time']

STATIC_RESOURCES = []

PHYSICAL_CONSTANTS = {
    # Source: https://en.wikipedia.org/wiki/Speed_of_light
    'c': 299792458,  # speed of light [m/s]

    # All distances in meters.

    # Time-averaged distance between the Earth and lunar surfaces. The average distance between the Earth and Moon is
    # 384,400 km but the radius of the Earth is 6,371 km and the radius of the Moon is 1,737 km, so in this case light
    # actually travels 384,400 - 6,371, - 1,737 = 376,292 km
    # Source: https://en.wikipedia.org/wiki/Lunar_distance_(astronomy)
    'd_Earth_Moon': 376292e3,  # 376,292 km

    # 1 Astronomical unit (almost equal to the average of Earth's aphelion and perihelion).
    # Source: https://en.wikipedia.org/wiki/Astronomical_unit
    'd_Sun_Earth': 149597870700.0,  # ~150 million kilometres

    # Maximum distance between the Earth and Mars.
    # Source: https://www.space.com/14729-spacekids-distance-earth-mars.html
    'd_Earth_Mars': 401e9,  # ~401 million km

    # Maximum distance between Earth and Jupiter.
    # Source: https://www.universetoday.com/14514/how-far-is-jupiter-from-earth/
    'd_Earth_Jupiter': 928e9,  # ~928 million km
}

ATOL = {}
RTOL = {
    'time': 1e-5
}


class TestCaseType(TestCaseTypeEnum):
    EARTH_TO_MOON = ("Earth to moon", 1)
    SUN_TO_EARTH = ("Sun to Earth", 1)
    MAX_EARTH_TO_MARS = ("Earth to Mars", 1)
    MAX_EARTH_TO_JUPITER = ("Earth to Jupiter", 1)
    RANDOM = ("Random", 1)


class ProblemTestCase(TestCase):
    def input_tuple(self) -> tuple:
        return self.input['distance'],

    def output_tuple(self) -> tuple:
        return self.output['time'],

    def output_str(self) -> str:
        return str(self.output['time'])


def generate_test_case(test_type: TestCaseType) -> ProblemTestCase:
    test_case = ProblemTestCase(test_type)

    if test_type is TestCaseType.EARTH_TO_MOON:
        distance = PHYSICAL_CONSTANTS['d_Earth_Moon']

    elif test_type is TestCaseType.SUN_TO_EARTH:
        distance = PHYSICAL_CONSTANTS['d_Sun_Earth']

    elif test_type is TestCaseType.MAX_EARTH_TO_MARS:
        distance = PHYSICAL_CONSTANTS['d_Earth_Mars']

    elif test_type is TestCaseType.MAX_EARTH_TO_JUPITER:
        distance = PHYSICAL_CONSTANTS['d_Earth_Jupiter']

    elif test_type is TestCaseType.RANDOM:
        c = PHYSICAL_CONSTANTS['c']
        distance = uniform(c, 60*c)

    test_case.input['distance'] = distance
    test_case.output['time'] = light_time(distance)

    return test_case
