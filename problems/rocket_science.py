import numpy as np

from problems.test_case import TestCase, TestCaseTypeEnum

from os import path
import logging.config
import logging


logging_config_path = path.join(path.dirname(path.abspath(__file__)), '..', 'logging.ini')
logging.config.fileConfig(logging_config_path)
logger = logging.getLogger(__name__)


class TestCaseI1Type(TestCaseTypeEnum):
    EARTH = ('Earth', '', 1)
    MOON = ('Moon', '', 1)
    JUPITER = ('Jupiter', '', 1)
    PLUTO = ('Pluto', '', 1)
    PHOBOS = ('Phobos', '', 1)
    # TITAN = ('Titan', '', 1)
    # HALLEY = ('Halley\'s comet', '', 1)
    RANDOM = ('Random', '', 1)


class TestCaseI1(TestCase):
    def input_str(self) -> str:
        return str(self.input['v'])

    def output_str(self) -> str:
        return '\n'.join(map(str, self.output['x']))


TEST_CASE_TYPE_ENUM = TestCaseI1Type
TEST_CASE_CLASS = TestCaseI1

PHYSICAL_CONSTANTS = {}
TESTING_CONSTANTS = {}


def generate_input(test_type: TestCaseI1Type) -> TestCaseI1:
    test_case = TestCaseI1(test_type)

    if test_type is TestCaseI1Type.EARTH:
        v = 11.186
    elif test_type is TestCaseI1Type.MOON:
        v = 2.38
    elif test_type is TestCaseI1Type.JUPITER:
        v = 60.20
    elif test_type is TestCaseI1Type.PLUTO:
        v = 1.23
    elif test_type is TestCaseI1Type.PHOBOS:
        v = 0.001139
    elif test_type is TestCaseI1Type.RANDOM:
        v = np.random.uniform(1.0, 100.0, 1)

    test_case.input['v'] = v
    return test_case


def solve_test_case(test_case: TestCaseI1) -> None:
    v = test_case.input['v']
    M = PHYSICAL_CONSTANTS['M']
    v_e = PHYSICAL_CONSTANTS['v_e']

    test_case.output['m_fuel'] = M*(np.exp(v/v_e) - 1)
    return


def verify_user_solution(user_input_str: str, user_output_str: str) -> bool:
    pass
