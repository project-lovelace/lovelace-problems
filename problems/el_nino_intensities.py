import logging

import numpy as np

from problems.test_case import TestCase, TestCaseTypeEnum

logger = logging.getLogger(__name__)


class TestCaseType(TestCaseTypeEnum):
    RANDOM_SEASON = ('Random season', 5)


class ProblemTestCase(TestCase):
    def input_tuple(self) -> tuple:
        return (self.input["season"],)

    def output_tuple(self) -> tuple:
        return (self.output['enso_classification'],)


FUNCTION_NAME = "enso_classification"
STATIC_RESOURCES = ['mei.ext_index.txt']

PHYSICAL_CONSTANTS = {}
TESTING_CONSTANTS = {
    'mei_tol': 1e-3
}


def generate_test_case(test_type: TestCaseType) -> ProblemTestCase:
    test_case = ProblemTestCase(test_type)
    if test_type is TestCaseType.RANDOM_SEASON:
        year = np.random.randint(1871, 2015)
        next_year_short = str(year+1)[-2:]
        season = str(year) + '-' + next_year_short

    test_case.input['season'] = season
    return test_case


def solve_test_case(test_case: ProblemTestCase) -> None:
    from problems.solutions.el_nino_intensities import enso_classification
    season = test_case.input['season']
    test_case.output['enso_classification'] = enso_classification(season)
    return


def verify_user_solution(user_input: tuple, user_output: tuple) -> bool:
    logger.info("Verifying user solution...")
    logger.debug("User input string: %s", user_input)
    logger.debug("User output string: %s", user_output)

    # Build TestCase object out of user's input string.
    tmp_test_case = ProblemTestCase()

    season = user_input[0]
    tmp_test_case.input = {"season": season}

    # Solve the problem with this TestCase so we have our own solution, and extract the solution.
    solve_test_case(tmp_test_case)
    classification, intensity, mei = tmp_test_case.output['enso_classification']

    # Extract user solution.
    user_classification, user_intensity, user_mei = user_output

    logger.debug("User solution:")
    logger.debug("{:}, {:}, {:}".format(user_classification, user_intensity, user_mei))
    logger.debug("Engine solution:")
    logger.debug("{:}, {:}, {:}".format(classification, intensity, mei))

    mei_tol = TESTING_CONSTANTS["mei_tol"]
    if user_classification == classification and user_intensity == intensity and abs(user_mei - mei) < mei_tol:
        user_solution_correct = True
    else:
        user_solution_correct = False

    passed = False

    if user_solution_correct:
        logger.info("User solution correct.")
        passed = True
    else:
        logger.info("User solution incorrect.")

    return passed, "classification = {}, intensity = {}, mei = {}".format(classification, intensity, mei)
