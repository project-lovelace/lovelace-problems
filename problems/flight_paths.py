import logging
from typing import Tuple

from numpy.random import uniform

from problems.test_case import TestCase, TestCaseTypeEnum, test_case_solution_correct
from problems.solutions.flight_paths import haversine

logger = logging.getLogger(__name__)

FUNCTION_NAME = "haversine"
INPUT_VARS = ['lat1', 'lon1', 'lat2', 'lon2']
OUTPUT_VARS = ['distance']

STATIC_RESOURCES = []

PHYSICAL_CONSTANTS = {
    'R': 6372.1  # Radius of the Earth [km]
}
ATOL = {}
RTOL = {
    'distance': 1e-5
}


class TestCaseType(TestCaseTypeEnum):
    RANDOM_POINTS = ("Two random points", 2)


class ProblemTestCase(TestCase):
    def input_tuple(self) -> tuple:
        return self.input['lat1'], self.input['lon1'], self.input['lat2'], self.input['lon2']

    def output_tuple(self) -> tuple:
        return self.output['distance'],

    def output_str(self) -> str:
        return str(self.output['distance'])


def generate_test_case(test_type: TestCaseType) -> ProblemTestCase:
    test_case = ProblemTestCase(test_type)

    if test_type is TestCaseType.RANDOM_POINTS:
        lat1 = uniform(-90, 90)
        lon1 = uniform(-180, 180)
        lat2 = uniform(-90, 90)
        lon2 = uniform(-180, 180)

    test_case.input = {
        "lat1": lat1,
        "lon1": lon1,
        "lat2": lat2,
        "lon2": lon2
    }

    return test_case


def solve_test_case(test_case: ProblemTestCase) -> None:
    lat1, lon1 = test_case.input['lat1'], test_case.input['lon1']
    lat2, lon2 = test_case.input['lat2'], test_case.input['lon2']
    test_case.output['distance'] = haversine(lat1, lon1, lat2, lon2)


def verify_user_solution(user_input: tuple, user_output: tuple) -> Tuple[bool, str]:
    user_test_case = ProblemTestCase(None, INPUT_VARS, user_input, OUTPUT_VARS, user_output)
    passed, correct_test_case = test_case_solution_correct(user_test_case, ATOL, RTOL, ProblemTestCase, solve_test_case)
    return passed, correct_test_case.output_str()
