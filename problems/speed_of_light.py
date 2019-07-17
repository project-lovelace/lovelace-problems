import logging
from typing import Tuple
from numpy.random import uniform

from problems.test_case import TestCase, TestCaseTypeEnum, test_case_solution_correct
from problems.solutions.speed_of_light import light_time

logger = logging.getLogger(__name__)

FUNCTION_NAME = "light_time"
INPUT_VARS = ['distance']
OUTPUT_VARS = ['time']

STATIC_RESOURCES = []

PHYSICAL_CONSTANTS = {
    'c': 299792458  # speed of light [m/s]
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
        distance = 385000e3  # 385,000 km
    elif test_type is TestCaseType.SUN_TO_EARTH:
        distance = 1.4959802296e11  # https://www.wolframalpha.com/input/?i=mean+sun+to+earth+distance
    elif test_type is TestCaseType.MAX_EARTH_TO_MARS:
        distance = 401e9  # 401 million km
    elif test_type is TestCaseType.MAX_EARTH_TO_JUPITER:
        distance = 968e9  # 968 million km
    elif test_type is TestCaseType.RANDOM:
        distance = uniform(299792458, 60*299792458)

    test_case.input['distance'] = distance
    return test_case


def solve_test_case(test_case: ProblemTestCase) -> None:
    distance = test_case.input['distance']
    test_case.output['time'] = light_time(distance)


def verify_user_solution(user_input: tuple, user_output: tuple) -> Tuple[bool, str]:
    user_test_case = ProblemTestCase(None, INPUT_VARS, user_input, OUTPUT_VARS, user_output)
    passed, correct_test_case = test_case_solution_correct(user_test_case, ATOL, RTOL, ProblemTestCase, solve_test_case)
    return passed, correct_test_case.output_str()
