import logging
from typing import Tuple

from numpy.random import randint

from problems.test_case import TestCase, TestCaseTypeEnum
from problems.solutions.ada_lovelaces_note_g import bernoulli

logger = logging.getLogger(__name__)

FUNCTION_NAME = "bernoulli"
INPUT_VARS = ['n']
OUTPUT_VARS = ['numerator', 'denominator']

STATIC_RESOURCES = []

PHYSICAL_CONSTANTS = {}
ATOL = {}
RTOL = {}


class TestCaseType(TestCaseTypeEnum):
    ZEROTH = ("Zeroth Bernoulli number", 1)
    FIRST = ("First Bernoulli number", 1)
    SECOND = ("Second Bernoulli number", 1)
    THIRD = ("Third Bernoulli number", 1)
    RANDOM_EVEN = ("Even 2 < n < 50", 2)
    RANDOM_ODD = ("Odd 3 < n < 51", 2)
    LARGE_EVEN = ("Even 50 < n < 125", 1)
    LARGE_ODD = ("Odd 51 < n < 126", 1)


class ProblemTestCase(TestCase):
    def input_tuple(self) -> tuple:
        return self.input['n'],

    def output_tuple(self) -> tuple:
        numerator = self.output['numerator']
        denominator = self.output['denominator']
        return numerator, denominator


def generate_test_case(test_type: TestCaseType) -> ProblemTestCase:
    test_case = ProblemTestCase(test_type)

    if test_type is TestCaseType.ZEROTH:
        n = 0

    elif test_type is TestCaseType.FIRST:
        n = 1

    elif test_type is TestCaseType.SECOND:
        n = 2

    elif test_type is TestCaseType.THIRD:
        n = 3

    elif test_type is TestCaseType.RANDOM_EVEN:
        n = 2 * randint(2, 50)

    elif test_type is TestCaseType.RANDOM_ODD:
        n = 2 * randint(2, 50) + 1

    elif test_type is TestCaseType.LARGE_EVEN:
        n = 2 * randint(50, 125)

    elif test_type is TestCaseType.LARGE_ODD:
        n = 2 * randint(50, 125) + 1

    else:
        raise ValueError(f"Unrecognized test case: {test_type}")

    test_case.input['n'] = n
    test_case.output['numerator'], test_case.output['denominator'] = bernoulli(n)

    return test_case
