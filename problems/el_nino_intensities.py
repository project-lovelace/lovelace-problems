import logging
from typing import Tuple

from numpy.random import randint

from problems.test_case import TestCase, TestCaseTypeEnum, test_case_solution_correct

logger = logging.getLogger(__name__)


class TestCaseType(TestCaseTypeEnum):
    RANDOM_SEASON = ('Random season', 5)


class ProblemTestCase(TestCase):
    def input_tuple(self) -> tuple:
        return self.input["season"],

    def output_tuple(self) -> tuple:
        return self.output['enso_classification'],

    def output_str(self) -> str:
        return self.output['enso_classification']


FUNCTION_NAME = "enso_classification"
STATIC_RESOURCES = ["mei.ext_index.txt"]

INPUT_VARS = ['season']
OUTPUT_VARS = ['enso_classification']

PHYSICAL_CONSTANTS = {}

ATOL = {}
RTOL = {
    'enso_classification': 0.001
}


def generate_test_case(test_type: TestCaseType) -> ProblemTestCase:
    test_case = ProblemTestCase(test_type)
    if test_type is TestCaseType.RANDOM_SEASON:
        year = randint(1871, 2015)
        next_year_short = str(year+1)[-2:]
        season = str(year) + '-' + next_year_short

    test_case.input['season'] = season
    return test_case


def solve_test_case(test_case: ProblemTestCase) -> None:
    from problems.solutions.el_nino_intensities import enso_classification
    season = test_case.input['season']
    test_case.output['enso_classification'] = enso_classification(season)


def verify_user_solution(user_input: tuple, user_output: tuple) -> Tuple[bool, str]:
    user_test_case = ProblemTestCase(None, INPUT_VARS, user_input, OUTPUT_VARS, user_output)
    passed, correct_test_case = test_case_solution_correct(user_test_case, ATOL, RTOL, ProblemTestCase, solve_test_case)
    return passed, correct_test_case.output_str()
