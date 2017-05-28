import logging

from problems.test_case import TestCase, TestCaseTypeEnum

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('[%(asctime)s] %(name)s:%(levelname)s: %(message)s')


class TestCaseXType(TestCaseTypeEnum):
    EXAMPLE1 = ('Example1', 'Some description', 2)
    EXAMPLE2 = ('Example2', '', 1)


class TestCaseX(TestCase):
    def input_str(self) -> str:
        pass

    def output_str(self) -> str:
        pass


TEST_CASE_TYPE_ENUM = TestCaseXType
TEST_CASE_CLASS = TestCaseX

PHYSICAL_CONSTANTS = {}
TESTING_CONSTANTS = {}


def generate_input(test_type: TestCaseXType) -> TestCaseX:
    pass


def solve_test_case(test_case: TestCaseX) -> None:
    pass


def verify_user_solution(user_input_str: str, user_output_str: str) -> bool:
    pass
