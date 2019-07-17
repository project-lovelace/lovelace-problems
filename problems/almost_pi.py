import logging
from typing import Tuple

from numpy.random import randint

from problems.test_case import TestCase, TestCaseTypeEnum, test_case_solution_correct
from problems.solutions.almost_pi import almost_pi

logger = logging.getLogger(__name__)

FUNCTION_NAME = "almost_pi"
INPUT_VARS = ['N']
OUTPUT_VARS = ['pi']

STATIC_RESOURCES = []

PHYSICAL_CONSTANTS = {}
ATOL = {}
RTOL = {
    'pi': 1e-5
}


class TestCaseType(TestCaseTypeEnum):
    SMALL_N = ("1 < n < 10", 2)
    MEDIUM_N = ("10 < n < 100", 2)
    LARGE_N = ("100 < n < 1,000", 1)
    HUGE_N = ("10,000 < n < 20,000", 1)


class ProblemTestCase(TestCase):
    def input_tuple(self) -> tuple:
        return self.input['N'],

    def output_tuple(self) -> tuple:
        return self.output['pi'],

    def output_str(self) -> str:
        return str(self.output['pi'])


def generate_test_case(test_type: TestCaseType) -> ProblemTestCase:
    test_case = ProblemTestCase(test_type)

    if test_type is TestCaseType.SMALL_N:
        N = randint(2, 10)

    if test_type is TestCaseType.MEDIUM_N:
        N = randint(11, 100)

    if test_type is TestCaseType.LARGE_N:
        N = randint(101, 1000)

    if test_type is TestCaseType.HUGE_N:
        N = randint(10000, 100000)

    test_case.input['N'] = N
    return test_case


def solve_test_case(test_case: ProblemTestCase) -> None:
    N = test_case.input['N']
    test_case.output['pi'] = almost_pi(N)


def verify_user_solution(user_input: tuple, user_output: tuple) -> Tuple[bool, str]:
    user_test_case = ProblemTestCase(None, INPUT_VARS, user_input, OUTPUT_VARS, user_output)
    passed, correct_test_case = test_case_solution_correct(user_test_case, ATOL, RTOL, ProblemTestCase, solve_test_case)
    return passed, correct_test_case.output_str()
