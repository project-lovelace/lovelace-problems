import logging
from typing import Tuple

from numpy.random import randint

from problems.test_case import TestCase, TestCaseTypeEnum

logger = logging.getLogger(__name__)

FUNCTION_NAME = "enso_classification"
INPUT_VARS = ['year']
OUTPUT_VARS = ['enso_classification', 'enso_intensity']

STATIC_RESOURCES = ["mei.ext_index.txt"]

PHYSICAL_CONSTANTS = {}
ATOL = {}
RTOL = {}


class TestCaseType(TestCaseTypeEnum):
    QUIET_YEAR = ("Quiet year", 1)
    WEAK_EL_NINO = ("Weak El Niño", 1)
    WEAK_LA_NINA = ("Weak La Niña", 1)
    MODERATE_EL_NINO = ("Moderate El Niño", 1)
    MODERATE_LA_NINA = ("Moderate La Niña", 1)
    STRONG_EL_NINO = ("Strong El Niño", 1)
    STRONG_LA_NINA = ("Strong La Niña", 1)
    VERY_STRONG_EL_NINO = ("Very strong El Niño", 1)
    VERY_STRONG_LA_NINA = ("Very strong La Niña", 1)
    RANDOM_YEAR = ("Random year", 5)


class ProblemTestCase(TestCase):
    def input_tuple(self) -> tuple:
        return self.input["year"],

    def output_tuple(self) -> tuple:
        return self.output['enso_classification'], self.output['enso_intensity']


def generate_test_case(test_type: TestCaseType) -> ProblemTestCase:
    test_case = ProblemTestCase(test_type)

    if test_type is TestCaseType.QUIET_YEAR:
        year = 1996
    elif test_type is TestCaseType.WEAK_EL_NINO:
        year = 1948
    elif test_type is TestCaseType.WEAK_LA_NINA:
        year = 1871
    elif test_type is TestCaseType.MODERATE_EL_NINO:
        year = 1914
    elif test_type is TestCaseType.MODERATE_LA_NINA:
        year = 2000
    elif test_type is TestCaseType.STRONG_EL_NINO:
        year = 1993
    elif test_type is TestCaseType.STRONG_LA_NINA:
        year = 1890
    elif test_type is TestCaseType.VERY_STRONG_EL_NINO:
        year = 2016
    elif test_type is TestCaseType.VERY_STRONG_LA_NINA:
        year = 1955
    elif test_type is TestCaseType.RANDOM_YEAR:
        year = randint(1871, 2016)
    else:
        raise ValueError(f"Unrecognized test case: {test_type}")

    test_case.input['year'] = year

    from problems.solutions.el_nino_intensities import enso_classification
    classification, intensity = enso_classification(year)

    test_case.output['enso_classification'] = classification
    test_case.output['enso_intensity'] = intensity

    return test_case
