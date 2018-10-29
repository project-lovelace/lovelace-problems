import logging

from problems.test_case import TestCase, TestCaseTypeEnum

logger = logging.getLogger(__name__)


class TestCase9Type(TestCaseTypeEnum):
    EXTENDED_MEI = ('Extended MEI index', 1)


class TestCase9(TestCase):
    def input_tuple(self) -> tuple:
        return ()

    def output_tuple(self) -> str:
        return (self.output['classification_str'],)


TEST_CASE_TYPE_ENUM = TestCase9Type
TEST_CASE_CLASS = TestCase9
FUNCTION_NAME = "enso_classification"
STATIC_RESOURCES = ['mei.ext_index.txt']

PHYSICAL_CONSTANTS = {}
TESTING_CONSTANTS = {}


def generate_test_case(test_type: TestCase9Type) -> TestCase9:
    test_case = TestCase9(test_type)
    return test_case


def solve_test_case(test_case: TestCase9) -> None:
    import csv

    years = []
    mei = []

    with open('mei.ext_index.txt') as csvfile:
        reader = csv.reader(csvfile, delimiter='\t')
        next(reader, None)  # skip the header line
        for row in reader:
            years.append(int(row[0]))
            mei.append([float(i) for i in row[1:]])

    classification_str = ''
    for i in range(len(years) - 1):
        season = str(years[i])[:4] + '-' + str(years[i + 1])[-2:]
        season_mei = mei[i] + mei[i + 1]
        for j in range(len(season_mei) - 5):
            if all(idx >= 0.5 for idx in season_mei[j:j + 5]):
                max_mei = max(season_mei)
                classification_str = classification_str + '{}: El Nino (MEI={})'.format(season, max_mei) + '\n'
                break
            elif all(idx <= -0.5 for idx in season_mei[j:j + 5]):
                min_mei = min(season_mei)
                classification_str = classification_str + '{}: La Nina (MEI={})'.format(season, min_mei) + '\n'
                break

    test_case.output['classification_str'] = classification_str[:-1]  # remove newline from the end
    return


def verify_user_solution(user_input: tuple, user_output: tuple) -> bool:
    logger.info("Verifying user solution...")
    logger.debug("User input string: %s", user_input)
    logger.debug("User output string: %s", user_output)

    # Build TestCase object out of user's input string.
    tmp_test_case = TestCase9()

    # Solve the problem with this TestCase so we have our own solution, and extract the solution.
    solve_test_case(tmp_test_case)
    classification_str = tmp_test_case.output['classification_str']

    # Extract user solution.
    user_classification_str = user_output[0]

    logger.debug("User solution:")
    logger.debug("{:s}".format(user_classification_str))
    logger.debug("Engine solution:")
    logger.debug("{:s}".format(classification_str))

    user_solution_correct = True
    for i in range(len(classification_str)):
        if classification_str[i] != user_classification_str[i]:
            user_solution_correct = False
            break

    if user_solution_correct:
        logger.info("User solution correct.")
        return True
    else:
        logger.info("User solution incorrect.")
        return False
