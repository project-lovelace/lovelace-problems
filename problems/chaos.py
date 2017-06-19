import numpy as np

from problems.test_case import TestCase, TestCaseTypeEnum

from os import path
import logging.config
import logging


logging_config_path = path.join(path.dirname(path.abspath(__file__)), '..', 'logging.ini')
logging.config.fileConfig(logging_config_path)
logger = logging.getLogger(__name__)


class TestCase9Type(TestCaseTypeEnum):
    DEATH = ('death', '', 1)
    QUICK_STABLE = ('quick stable', '', 1)
    FLUCTUATE_STABLE = ('fluctuate stable', '', 1)
    OSCILLATION = ('oscillation', '', 1)
    CHAOS = ('chaos', '', 1)
    DIVERGENCE = ('divergence', '', 1)


class TestCase9(TestCase):
    def input_str(self) -> str:
        return str(self.input['r'])

    def output_str(self) -> str:
        return '\n'.join(map(str, self.output['x']))


TEST_CASE_TYPE_ENUM = TestCase9Type
TEST_CASE_CLASS = TestCase9

PHYSICAL_CONSTANTS = {}
TESTING_CONSTANTS = {}


def generate_input(test_type: TestCase9Type) -> TestCase9:
    test_case = TestCase9(test_type)

    if test_type is TestCase9Type.DEATH:
        r = 1
    elif test_type is TestCase9Type.QUICK_STABLE:
        r = 2
    elif test_type is TestCase9Type.FLUCTUATE_STABLE:
        r = 3
    elif test_type is TestCase9Type.OSCILLATION:
        r = 4
    elif test_type is TestCase9Type.CHAOS:
        r = 5
    elif test_type is TestCase9Type.DIVERGENCE:
        r = 6

    test_case.input['r'] = r
    return test_case


def solve_test_case(test_case: TestCase9) -> None:
    r = test_case.input['r']

    x = [0.5]
    for _ in range(50):
        x.append(r*x[-1]*(1-x[-1]))

    test_case.output['x'] = x
    return


def verify_user_solution(user_input_str: str, user_output_str: str) -> bool:
    pass
