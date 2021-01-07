import logging
from typing import Tuple

from numpy.random import uniform

from problems.test_case import TestCase, TestCaseTypeEnum
from problems.solutions.sha_256 import SHA256

logger = logging.getLogger(__name__)

FUNCTION_NAME = "SHA256"
INPUT_VARS = ['message']
OUTPUT_VARS = ['digest']

STATIC_RESOURCES = []

PHYSICAL_CONSTANTS = {}
ATOL = {}
RTOL = {}


class TestCaseType(TestCaseTypeEnum):
    EMPTY_STRING = ("Empty string", 1)
    ABC = ("ABC", 1)
    QUICK_BROWN_FOX = ("Quick brown fox", 1)


class ProblemTestCase(TestCase):
    def input_tuple(self) -> tuple:
        return self.input['message'],

    def output_tuple(self) -> tuple:
        return self.output['digest'],


def generate_test_case(test_type: TestCaseType) -> ProblemTestCase:
    test_case = ProblemTestCase(test_type)

    if test_type is TestCaseType.EMPTY_STRING:
        M = ""

    elif test_type is TestCaseType.ABC:
        M = "ABC"

    elif test_type is TestCaseType.QUICK_BROWN_FOX:
        M = "The quick brown fox jumps over the lazy dog"

    test_case.input['message'] = M
    test_case.output['digest'] = SHA256(M)

    return test_case
