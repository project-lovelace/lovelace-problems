import math
import logging

import numpy as np

from problems.test_case import TestCase, TestCaseTypeEnum

logger = logging.getLogger(__name__)


class TestCaseType(TestCaseTypeEnum):
    EARTH_TO_MOON = ("Earth to moon", 1)
    SUN_TO_EARTH = ("Sun to Earth", 1)
    MAX_EARTH_TO_MARS = ("Earth to Mars", 1)
    MAX_EARTH_TO_JUPITER = ("Earth to Jupiter", 1)
    RANDOM = ("Random", 1)


class ProblemTestCase(TestCase):
    def input_tuple(self) -> tuple:
        return self.input["distance"]

    def output_tuple(self) -> tuple:
        return self.output["time"]


TEST_CASE_TYPE_ENUM = TestCaseType
TEST_CASE_CLASS = ProblemTestCase
FUNCTION_NAME = "light_time"
STATIC_RESOURCES = []

PHYSICAL_CONSTANTS = {
    "c": 299792458  # [m/s]
}
TESTING_CONSTANTS = {
    "rel_tol": 1e-5
}


def generate_test_case(test_type: TestCaseType) -> ProblemTestCase:
    test_case = ProblemTestCase(test_type)

    if test_type is TestCaseType.EARTH_TO_MOON:
        distance = 385000e3  # 385,000 km
    elif test_type is TestCaseType.SUN_TO_EARTH:
        distance = 1.4959802296e11  # https://www.wolframalpha.com/input/?i=mean+sun+to+earth+distance
    elif test_type is TestCaseType.MAX_EARTH_TO_MARS:
        distance = 401e9  # 401 million km
    elif test_type is TestCaseType.EARTH_TO_JUPITER:
        distance = 968e9  # 968 million km
    elif test_type is TestCaseType.RANDOM:
        distance = np.random.uniform(299792458, 60*299792458)
    else:
        raise ValueError("Invalid test case type.")

    test_case.input["distance"] = distance

    return test_case


def solve_test_case(test_case: ProblemTestCase) -> None:
    c = PHYSICAL_CONSTANTS["c"]
    distance = test_case.input["distance"]
    test_case.output["time"] = distance / c
    return


def verify_user_solution(user_input: tuple, user_output: tuple) -> bool:
    logger.info("Verifying user solution...")
    logger.debug("User input tuple: %s", user_input)
    logger.debug("User output tuple: %s", user_output)

    tmp_test_case = ProblemTestCase()

    distance = user_input[0]
    tmp_test_case.input = {"distance": distance}

    solve_test_case(tmp_test_case)
    time = tmp_test_case.output["time"]

    user_time = user_output[0]

    logger.debug("User solution:")
    logger.debug("time = {:f}".format(user_time))
    logger.debug("Engine solution:")
    logger.debug("time = {:f}".format(time))
    logger.debug("Relative tolerance = {:g}.".format(TESTING_CONSTANTS["rel_tol"]))

    passed = False

    if math.isclose(time, user_time, rel_tol=TESTING_CONSTANTS["rel_tol"]):
        logger.info("User solution correct.")
        passed = True
    else:
        logger.info("User solution is wrong.")
        passed = False

    return passed, str(user_time)
