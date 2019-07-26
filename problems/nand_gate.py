import logging
from typing import Tuple

from problems.test_case import TestCase, TestCaseTypeEnum, test_case_solution_correct
from problems.solutions.nand_gate import NAND

logger = logging.getLogger(__name__)

FUNCTION_NAME = "NAND"
INPUT_VARS = ['p', 'q']
OUTPUT_VARS = ['nand']

STATIC_RESOURCES = []

PHYSICAL_CONSTANTS = {}
ATOL = {}
RTOL = {}


class TestCaseType(TestCaseTypeEnum):
    ZERO_ZERO = ("00", 1)
    ZERO_ONE = ("01", 1)
    ONE_ZERO = ("10", 1)
    ONE_ONE = ("11", 1)


class ProblemTestCase(TestCase):
    def input_tuple(self) -> tuple:
        return self.input['p'], self.input['q']

    def output_tuple(self) -> tuple:
        return self.output['nand'],

    def output_str(self) -> str:
        return self.output['nand']


def generate_test_case(test_type: TestCaseType) -> ProblemTestCase:
    test_case = ProblemTestCase(test_type)

    if test_type is TestCaseType.ZERO_ZERO:
        p, q = 0, 0

    elif test_type is TestCaseType.ZERO_ONE:
        p, q = 0, 1

    elif test_type is TestCaseType.ONE_ZERO:
        p, q = 1, 0

    elif test_type is TestCaseType.ONE_ONE:
        p, q = 1, 1

    test_case.input["p"], test_case.input["q"] = p, q
    test_case.output["nand"] = NAND(p, q)

    return test_case


def verify_user_solution(correct_test_case: TestCase, user_input: tuple, user_output: tuple) -> Tuple[bool, str]:
    user_test_case = ProblemTestCase(None, INPUT_VARS, user_input, OUTPUT_VARS, user_output)
    passed, correct_test_case = test_case_solution_correct(correct_test_case, user_test_case, ATOL, RTOL)
    return passed, correct_test_case.output_str()
