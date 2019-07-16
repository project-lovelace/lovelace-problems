import logging
from typing import Tuple

from numpy.random import randint

from problems.test_case import TestCase, TestCaseTypeEnum, test_case_solution_correct
from problems.solutions.ada_lovelaces_note_g import bernoulli

logger = logging.getLogger(__name__)


class TestCaseType(TestCaseTypeEnum):
    ZEROTH = ("Zeroth Bernoulli number", 1)
    FIRST = ("First Bernoulli number", 1)
    SECOND = ("Second Bernoulli number", 1)
    THIRD = ("Third Bernoulli number", 1)
    RANDOM_EVEN = ("Even n > 2", 2)
    RANDOM_ODD = ("Odd n > 3", 2)
    LARGE_EVEN = ("Even n > 250", 1)
    LARGE_ODD = ("Odd n > 250", 1)


class ProblemTestCase(TestCase):
    def input_tuple(self) -> tuple:
        return self.input['n'],

    def output_tuple(self) -> tuple:
        numerator = self.output['numerator']
        denominator = self.output['denominator']
        return numerator, denominator

    def output_str(self) -> str:
        numerator = self.output['numerator']
        denominator = self.output['denominator']
        return "numerator = {:d}, denominator = {:d}".format(numerator, denominator)


FUNCTION_NAME = "bernoulli"
STATIC_RESOURCES = []

INPUT_VARS = ['n']
OUTPUT_VARS = ['numerator', 'denominator']

PHYSICAL_CONSTANTS = {}
ATOL = {}
RTOL = {}


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
        n = 2 * randint(125, 250)
    elif test_type is TestCaseType.LARGE_ODD:
        n = 2 * randint(125, 250) + 1

    test_case.input['n'] = n
    return test_case


def solve_test_case(test_case: ProblemTestCase) -> None:
    n = test_case.input['n']
    test_case.output['numerator'], test_case.output['denominator'] = bernoulli(n)


def verify_user_solution(user_input: tuple, user_output: tuple) -> Tuple[bool, str]:
    user_test_case = ProblemTestCase(None, INPUT_VARS, user_input, OUTPUT_VARS, user_output)
    passed, correct_test_case = test_case_solution_correct(user_test_case, ATOL, RTOL, ProblemTestCase, solve_test_case)
    return passed, correct_test_case.output_str()