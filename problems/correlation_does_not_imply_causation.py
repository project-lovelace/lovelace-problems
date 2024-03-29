import os
import csv
import logging
from typing import Tuple

from numpy import array
from numpy.random import rand, randint

from problems.test_case import TestCase, TestCaseTypeEnum
from problems.solutions.correlation_does_not_imply_causation import correlation_coefficient

logger = logging.getLogger(__name__)

FUNCTION_NAME = "correlation_coefficient"
INPUT_VARS = ['x', 'y']
OUTPUT_VARS = ['r']

STATIC_RESOURCES = ["spurious_xy.csv"]

PHYSICAL_CONSTANTS = {}
ATOL = {
    'r': 0.0001
}
RTOL = {}


class TestCaseType(TestCaseTypeEnum):
    SPURIOUS_DATASET = ('spurious dataset', 1)
    RANDOM_DATASET = ('random dataset', 1)
    UNKNOWN = ('unknown case', 0)


class ProblemTestCase(TestCase):
    def input_tuple(self) -> tuple:
        return self.input['x'], self.input['y']

    def output_tuple(self) -> tuple:
        return self.output['r']


def write_random_dataset_csv(x, y):
    cwd = os.path.dirname(os.path.abspath(__file__))
    csv_filename = os.path.join(cwd, "..", "resources", "correlation_does_not_imply_causation", "random_xy.csv")
    with open(csv_filename, 'w') as outfile:
        xy_writer = csv.writer(outfile, delimiter=',')
        for i in range(len(x)):
            xy_writer.writerow((x[i], y[i]))


def generate_test_case(test_type: TestCaseType) -> ProblemTestCase:
    test_case = ProblemTestCase(test_type)

    if test_type is TestCaseType.SPURIOUS_DATASET:
        csv_filepath = "../resources/correlation_does_not_imply_causation/spurious_xy.csv"
        x = []
        y = []

        with open(csv_filepath) as csvfile:
            xy_reader = csv.reader(csvfile, delimiter=',')
            for row in xy_reader:
                x.append(float(row[0]))
                y.append(float(row[1]))

        dataset_filename = "spurious_xy.csv"

    elif test_type is TestCaseType.RANDOM_DATASET:
        N = randint(10, 100)
        x = rand(N).tolist()
        y = rand(N).tolist()
        write_random_dataset_csv(x, y)
        dataset_filename = "random_xy.csv"
        test_case.input['DYNAMIC_RESOURCES'] = [dataset_filename]

    else:
        raise ValueError(f"Unrecognized test case: {test_type}")

    test_case.input['x'] = x
    test_case.input['y'] = y
    test_case.input['dataset_filename'] = dataset_filename
    test_case.output['r'] = correlation_coefficient(x, y)

    return test_case
