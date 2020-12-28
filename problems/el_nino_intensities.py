import logging
from typing import Tuple

from numpy.random import randint

from problems.test_case import TestCase, TestCaseTypeEnum

logger = logging.getLogger(__name__)

FUNCTION_NAME = "enso_classification"
INPUT_VARS = ['season']
OUTPUT_VARS = ['enso_classification', 'enso_intensity', 'mei']

STATIC_RESOURCES = ["mei.ext_index.txt"]

PHYSICAL_CONSTANTS = {}
ATOL = {}
RTOL = {}


class TestCaseType(TestCaseTypeEnum):
    RANDOM_SEASON = ('Random season', 5)


class ProblemTestCase(TestCase):
    def input_tuple(self) -> tuple:
        return self.input["season"],

    def output_tuple(self) -> tuple:
        return self.output['enso_classification'], self.output['enso_intensity'], self.output['mei']

    def output_str(self) -> str:
        c, i, mei = self.output['enso_classification'], self.output['enso_intensity'], self.output['mei']
        return "classification={:}, intensity={:}, mei={:}".format(c, i, mei)


def generate_test_case(test_type: TestCaseType) -> ProblemTestCase:
    test_case = ProblemTestCase(test_type)

    if test_type is TestCaseType.RANDOM_SEASON:
        year = randint(1871, 2015)
        next_year_short = str(year+1)[-2:]
        season = str(year) + '-' + next_year_short

    test_case.input['season'] = season

    from problems.solutions.el_nino_intensities import enso_classification
    c, i, mei = enso_classification(season)

    test_case.output['enso_classification'] = c
    test_case.output['enso_intensity'] = i
    test_case.output['mei'] = mei

    return test_case
