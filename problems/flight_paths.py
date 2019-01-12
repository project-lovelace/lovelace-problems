import math
import logging

import numpy as np

from problems.test_case import TestCase, TestCaseTypeEnum

logger = logging.getLogger(__name__)


class TestCaseType(TestCaseTypeEnum):
    RANDOM_POINTS = ("Two random points", 2)


class ProblemTestCase(TestCase):
    def input_tuple(self) -> tuple:
        return self.input["lat1"], self.input["lon1"], self.input["lat2"], self.input["lon2"]

    def output_tuple(self) -> tuple:
        return (self.output["distance"],)


TEST_CASE_TYPE_ENUM = TestCaseType
TEST_CASE_CLASS = ProblemTestCase
FUNCTION_NAME = "haversine"
STATIC_RESOURCES = []

PHYSICAL_CONSTANTS = {
    "R": 6372.1  # Radius of the Earth [km]
}
TESTING_CONSTANTS = {
    "rel_tol": 1e-5
}


def generate_test_case(test_type: TestCaseType) -> ProblemTestCase:
    test_case = ProblemTestCase(test_type)

    if test_type is TestCaseType.RANDOM_POINTS:
        lat1 = np.random.uniform(-90, 90)
        lon1 = np.random.uniform(-180, 180)
        lat2 = np.random.uniform(-90, 90)
        lon2 = np.random.uniform(-180, 180)
    else:
        raise ValueError("Invalid test case type.")

    test_case.input = {
        "lat1": lat1,
        "lon1": lon1,
        "lat2": lat2,
        "lon2": lon2
    }

    return test_case


def solve_test_case(test_case: ProblemTestCase) -> None:
    from math import radians, sin, cos, sqrt, asin

    R = PHYSICAL_CONSTANTS["R"]

    lat1, lon1 = test_case.input["lat1"], test_case.input["lon1"]
    lat2, lon2 = test_case.input["lat2"], test_case.input["lon2"]

    dLat = radians(lat2 - lat1)
    dLon = radians(lon2 - lon1)
    lat1 = radians(lat1)
    lat2 = radians(lat2)

    a = sin(dLat/2)**2 + cos(lat1) * cos(lat2) * sin(dLon/2)**2
    c = 2 * asin(sqrt(a))

    test_case.output["distance"] = R*c
    return


def verify_user_solution(user_input: tuple, user_output: tuple) -> bool:
    logger.info("Verifying user solution...")
    logger.debug("User input tuple: %s", user_input)
    logger.debug("User output tuple: %s", user_output)

    tmp_test_case = ProblemTestCase()

    lat1, lon1, lat2, lon2 = user_input

    tmp_test_case.input = {
        "lat1": lat1,
        "lon1": lon1,
        "lat2": lat2,
        "lon2": lon2
    }

    solve_test_case(tmp_test_case)
    distance = tmp_test_case.output["distance"]

    user_distance = user_output[0]

    logger.debug("User solution:")
    logger.debug("distance = {:d}".format(user_distance))
    logger.debug("Engine solution:")
    logger.debug("distance = {:d}".format(distance))
    logger.debug("Relative tolerance = {:g}.".format(TESTING_CONSTANTS["rel_tol"]))

    passed = False

    if math.isclose(distance, user_distance, rel_tol=TESTING_CONSTANTS["rel_tol"]):
        logger.info("User solution correct.")
        passed = True
    else:
        logger.info("User solution is wrong.")
        passed = False

    return passed, str(distance)
