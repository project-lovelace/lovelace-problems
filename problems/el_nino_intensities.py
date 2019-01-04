import logging

import numpy as np

from problems.test_case import TestCase, TestCaseTypeEnum

logger = logging.getLogger(__name__)


class TestCase9Type(TestCaseTypeEnum):
    RANDOM_SEASON = ('Random season', 5)


class TestCase9(TestCase):
    def input_tuple(self) -> tuple:
        return (self.input["season"],)

    def output_tuple(self) -> tuple:
        return (self.output['enso_classification'],)


TEST_CASE_TYPE_ENUM = TestCase9Type
TEST_CASE_CLASS = TestCase9
FUNCTION_NAME = "enso_classification"
STATIC_RESOURCES = ['mei.ext_index.txt']

PHYSICAL_CONSTANTS = {}
TESTING_CONSTANTS = {
    'mei_tol': 1e-3
}


def generate_test_case(test_type: TestCase9Type) -> TestCase9:
    test_case = TestCase9(test_type)
    if test_type is TestCase9Type.RANDOM_SEASON:
        year = np.random.randint(1871, 2015)
        next_year_short = str(year+1)[-2:]
        season = str(year) + '-' + next_year_short

    test_case.input["season"] = season
    return test_case


def solve_test_case(test_case: TestCase9) -> None:
    import csv

    years = []
    mei = []

    def mei_to_intensity(mei_val):
        mei_val = abs(mei_val)
        if mei_val < 0.5:
            return "none"
        elif 0.5 <= mei_val < 1.0:
            return "weak"
        elif 1.0 <= mei_val < 1.5:
            return "moderate"
        elif 1.5 <= mei_val < 2.0:
            return "strong"
        elif 2.0 <= mei_val:
            return "very strong"

    with open('mei.ext_index.txt') as csvfile:
        reader = csv.reader(csvfile, delimiter='\t')
        next(reader, None)  # skip the header line
        for row in reader:
            years.append(int(row[0]))
            mei.append([float(i) for i in row[1:]])

    mei_dict = {}
    for i in range(len(years) - 1):
        season = str(years[i])[:4] + '-' + str(years[i + 1])[-2:]
        season_mei = mei[i] + mei[i+1]
        for j in range(len(season_mei) - 5):
            if all(idx >= 0.5 for idx in season_mei[j:j + 5]):
                max_mei = max(season_mei)

                mei_dict[season] = ("El Nino", mei_to_intensity(max_mei), max_mei)
                break
            elif all(idx <= -0.5 for idx in season_mei[j:j + 5]):
                min_mei = min(season_mei)
                mei_dict[season] = ("La Nina", mei_to_intensity(min_mei), min_mei)
                break
            else:
                mei_dict[season] = ("Neither", "none", 0)

    test_case.output["enso_classification"] = mei_dict[test_case.input["season"]]
    return


def verify_user_solution(user_input: tuple, user_output: tuple) -> bool:
    logger.info("Verifying user solution...")
    logger.debug("User input string: %s", user_input)
    logger.debug("User output string: %s", user_output)

    # Build TestCase object out of user's input string.
    tmp_test_case = TestCase9()

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
