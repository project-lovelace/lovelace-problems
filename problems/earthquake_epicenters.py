import logging
from typing import Tuple

from numpy import array, pi, sin, cos
from numpy.linalg import norm
from numpy.random import uniform, choice

from problems.test_case import TestCase, TestCaseTypeEnum
from problems.solutions.earthquake_epicenters import earthquake_epicenter

logger = logging.getLogger(__name__)

FUNCTION_NAME = "earthquake_epicenter"
INPUT_VARS = ['x1', 'y1', 't1', 'x2', 'y2', 't2', 'x3', 'y3', 't3']
OUTPUT_VARS = ['x', 'y']

STATIC_RESOURCES = []

PHYSICAL_CONSTANTS = {
    'v': 6.0  # velocity of seismic waves [km/s]
}

ATOL = {
    'x': 0.0001,  # [km]
    'y': 0.0001   # [km]
}
RTOL = {}


class TestCaseType(TestCaseTypeEnum):
    GENERAL = ("General case", 3)
    ZERO_CASE = ("Zero case", 1)
    EQUIDISTANT = ("Equidistant case", 1)


class ProblemTestCase(TestCase):
    def input_tuple(self) -> tuple:
        return (self.input['x1'], self.input['y1'], self.input['t1'],
                self.input['x2'], self.input['y2'], self.input['t2'],
                self.input['x3'], self.input['y3'], self.input['t3'])

    def output_tuple(self) -> tuple:
        return self.output['x'], self.output['y']


def generate_test_case(test_type: TestCaseType) -> ProblemTestCase:
    test_case = ProblemTestCase(test_type)

    if test_type is TestCaseType.GENERAL:
        r0 = uniform(-100, 100, 2)
        r1 = uniform(-100, 100, 2)
        r2 = uniform(-100, 100, 2)
        r3 = uniform(-100, 100, 2)

    elif test_type is TestCaseType.ZERO_CASE:
        r0 = uniform(-100, 100, 2)
        zero_station = choice([1, 2, 3])
        if zero_station == 1:
            r1 = r0
            r2 = uniform(-100, 100, 2)
            r3 = uniform(-100, 100, 2)
        elif zero_station == 2:
            r1 = uniform(-100, 100, 2)
            r2 = r0
            r3 = uniform(-100, 100, 2)
        else:
            r1 = uniform(-100, 100, 2)
            r2 = uniform(-100, 100, 2)
            r3 = r0

    elif test_type is TestCaseType.EQUIDISTANT:
        r0 = uniform(-10, 10, 2)  # Place the earthquake near the origin.
        d = uniform(10, 90)  # Distance to all the stations. Max=90 ensures we stay inside the box.
        theta = uniform(0, 2*pi, 3)  # Choose three angles to place the stations at a distance d away.

        r1 = r0 + d * array([cos(theta[0]), sin(theta[0])])
        r2 = r0 + d * array([cos(theta[1]), sin(theta[1])])
        r3 = r0 + d * array([cos(theta[2]), sin(theta[2])])

    v = PHYSICAL_CONSTANTS['v']

    t1 = norm(r1-r0) / v
    t2 = norm(r2-r0) / v
    t3 = norm(r3-r0) / v

    # Convert to float so the user gets Python floats and not numpy floats.
    test_case.input = {
        'x1': float(r1[0]),
        'y1': float(r1[1]),
        't1': float(t1),
        'x2': float(r2[0]),
        'y2': float(r2[1]),
        't2': float(t2),
        'x3': float(r3[0]),
        'y3': float(r3[1]),
        't3': float(t3)
    }

    # We already know the solution by constructions.
    test_case.output['x'] = r0[0]
    test_case.output['y'] = r0[1]

    return test_case
