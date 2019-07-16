import csv
import logging
import os

import numpy as np

from problems.test_case import TestCase, TestCaseTypeEnum
from problems.solutions.correlation_does_not_imply_causation import correlation_coefficient

logger = logging.getLogger(__name__)


class TestCase7Type(TestCaseTypeEnum):
    SPURIOUS_DATASET = ('spurious dataset', 1)
    RANDOM_DATASET = ('random dataset', 1)
    UNKNOWN = ('unknown case', 0)


class TestCase7(TestCase):
    def input_tuple(self) -> str:
        return (self.input['x'], self.input['y'])

    def output_tuple(self) -> str:
        return str(self.output['r'])


TEST_CASE_TYPE_ENUM = TestCase7Type
TEST_CASE_CLASS = TestCase7
FUNCTION_NAME = "correlation_coefficient"
STATIC_RESOURCES = ['spurious_xy.csv']

PHYSICAL_CONSTANTS = {}

TESTING_CONSTANTS = {
    'error_tol': 0.0001  # tolerance on correlation coefficient
}


def write_random_dataset_csv(x, y):
    cwd = os.path.dirname(os.path.abspath(__file__))
    csv_filename = os.path.join(cwd, '..', 'resources', 'correlation_does_not_imply_causation', 'random_xy.csv')
    with open(csv_filename, 'w') as outfile:
        xy_writer = csv.writer(outfile, delimiter=',')
        for i in range(len(x)):
            xy_writer.writerow((x[i], y[i]))


def generate_test_case(test_type: TestCase7Type) -> TestCase7:
    test_case = TestCase7(test_type)

    if test_type is TestCase7Type.SPURIOUS_DATASET:
        csv_filepath = '../resources/correlation_does_not_imply_causation/spurious_xy.csv'
        x = []
        y = []
        with open(csv_filepath) as csvfile:
            xy_reader = csv.reader(csvfile, delimiter=',')
            for row in xy_reader:
                x.append(float(row[0]))
                y.append(float(row[1]))
        dataset_filename = "spurious_xy.csv"
    elif test_type is TestCase7Type.RANDOM_DATASET:
        N = np.random.randint(10, 100)
        x = np.random.rand(N).tolist()
        y = np.random.rand(N).tolist()
        write_random_dataset_csv(x, y)
        dataset_filename = 'random_xy.csv'
        test_case.input['DYNAMIC_RESOURCES'] = [dataset_filename]
    else:
        raise ValueError

    test_case.input['x'] = x
    test_case.input['y'] = y
    test_case.input['dataset_filename'] = dataset_filename
    return test_case


def solve_test_case(test_case: TestCase7) -> None:
    x = np.array(test_case.input['x'])
    y = np.array(test_case.input['y'])
    test_case.output['r'] = correlation_coefficient(x, y)
    return


def verify_user_solution(user_input: tuple, user_output: tuple) -> bool:
    logger.info("Verifying user solution...")
    logger.debug("User input: %s", user_input)
    logger.debug("User output: %s", user_output)

    user_x, user_y = user_input

    # Build TestCase object out of user's input string.
    tmp_test_case = TestCase7()
    tmp_test_case.input['x'] = user_x
    tmp_test_case.input['y'] = user_y

    # Solve the problem with this TestCase so we have our own solution, and extract the solution.
    solve_test_case(tmp_test_case)
    r = tmp_test_case.output['r']

    # Extract user solution.
    user_r = user_output[0]

    error_tol = TESTING_CONSTANTS['error_tol']
    error_r = abs(r - user_r)

    logger.debug("User solution:")
    logger.debug("r = {}".format(user_r))
    logger.debug("Engine solution:")
    logger.debug("r = {}".format(r))
    logger.debug("Error tolerance = %e. Error r: %e.", error_tol, error_r)

    passed = False

    if error_r < error_tol:
        logger.info("User solution correct within error tolerance of {:g}.".format(error_tol))
        passed = True
    else:
        logger.info("User solution incorrect.")

    return passed, str(r)
