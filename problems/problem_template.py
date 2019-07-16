import logging

from problems.test_case import TestCase, TestCaseTypeEnum

logger = logging.getLogger(__name__)


class TestCaseType(TestCaseTypeEnum):
    EXAMPLE1 = ('Example1', 2)
    EXAMPLE2 = ('Example2', 1)


class ProblemTestCase(TestCase):
    def input_str(self) -> str:
        pass

    def output_str(self) -> str:
        pass


PHYSICAL_CONSTANTS = {}
TESTING_CONSTANTS = {}


def generate_input(test_type: TestCaseType) -> ProblemTestCase:
    pass


def solve_test_case(test_case: ProblemTestCase) -> None:
    pass


def verify_user_solution(user_input: tuple, user_output: tuple) -> bool:
    pass
