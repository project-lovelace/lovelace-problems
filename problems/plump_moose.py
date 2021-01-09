import logging

from numpy.random import uniform

from problems.test_case import TestCase, TestCaseTypeEnum
from problems.solutions.plump_moose import moose_body_mass

logger = logging.getLogger(__name__)

FUNCTION_NAME = "moose_body_mass"
INPUT_VARS = ["latitude"]
OUTPUT_VARS = ["mass"]

STATIC_RESOURCES = []
PHYSICAL_CONSTANTS = {}

ATOL = {}
RTOL = {
    "mass": 1e-6
}


class TestCaseType(TestCaseTypeEnum):
    MALMO = ("Moose from Malmö", 1)
    STOCKHOLM = ("Moose from Stockholm", 1)
    KIRUNA = ("Moose from Kiruna", 1)
    SOUTHERN = ("Southern moose", 1)
    NORTHERN = ("Northern moose", 1)
    RANDOM = ("Random", 2)


class ProblemTestCase(TestCase):
    def input_tuple(self):
        return self.input["latitude"],

    def output_tuple(self):
        return self.output["mass"],


def generate_test_case(test_type):
    test_case = ProblemTestCase(test_type)

    if test_type is TestCaseType.MALMO:
        latitude = 55.60587

    elif test_type is TestCaseType.STOCKHOLM:
        latitude = 59.33258

    elif test_type is TestCaseType.KIRUNA:
        latitude = 67.85507

    elif test_type is TestCaseType.SOUTHERN:
        latitude = uniform(58, 62)

    elif test_type is TestCaseType.NORTHERN:
        latitude = uniform(62, 66)

    elif test_type is TestCaseType.RANDOM:
        latitude = uniform(57, 67)

    else:
        raise ValueError(f"Unrecognized test case: {test_type}")

    test_case.input["latitude"] = latitude
    test_case.output["mass"] = moose_body_mass(latitude)

    return test_case
