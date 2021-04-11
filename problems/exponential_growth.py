import random
import logging

from problems.test_case import TestCase, TestCaseTypeEnum
from problems.solutions.exponential_growth import exponential_growth

logger = logging.getLogger(__name__)

FUNCTION_NAME = "exponential_growth"

INPUT_VARS = ["x0", "k", "dt", "N"]
OUTPUT_VARS = ["x"]

STATIC_RESOURCES = []

PHYSICAL_CONSTANTS = {}
ATOL = {}
RTOL = {}

class ProblemTestCase(TestCase):
    def input_tuple(self):
        return (self.input["x0"], self.input["k"], self.input["dt"], self.input["N"])

    def output_tuple(self):
        return self.output["x"],

class TestCaseType(TestCaseTypeEnum):
    NO_GROWTH_OR_DECAY = ("No growth or decay", 1)
    SLOW_GROWTH = ("Slow growth (small k)", 1)
    FAST_GROWTH = ("Fast growth (large k)", 1)
    DECAY = ("Exponential decay (k < 0)", 1)
    SMALL_TIME_STEPS = ("Small time steps (more accurate solution)", 1)
    LARGE_TIME_STEPS = ("Large time steps (less accurate solution)", 1)
    LONG_INTEGRATION = ("Long integration time", 1)
    NUMERICAL_NOISE = ("Numerical noise", 1)
    NUMERICAL_OSCILLATIONS = ("Numerical oscillations", 1)
    NUMERICAL_INSTABILITY = ("Numerical instability", 1)

def generate_test_case(test_type):
    test_case = ProblemTestCase(test_type)

    if test_type is TestCaseType.NO_GROWTH_OR_DECAY:
        x0 = random.uniform(-10, 10)
        k = 0
        dt = random.uniform(0.1, 1)
        N = random.randint(10, 15)

    elif test_type is TestCaseType.SLOW_GROWTH:
        x0 = random.uniform(-10, 10)
        k = random.uniform(0.01, 0.1)
        dt = random.uniform(0.1, 0.2)
        N = random.randint(20, 50)

    elif test_type is TestCaseType.FAST_GROWTH:
        x0 = random.uniform(-10, 10)
        k = random.uniform(4, 6)
        dt = random.uniform(0.1, 0.2)
        N = random.randint(20, 50)

    elif test_type is TestCaseType.DECAY:
        x0 = random.uniform(-10, 10)
        k = - random.uniform(1, 2)
        dt = random.uniform(0.1, 0.2)
        N = random.randint(20, 50)

    elif test_type is TestCaseType.SMALL_TIME_STEPS:
        x0 = random.uniform(1, 10)
        k = random.uniform(1, 1.2)
        dt = random.uniform(0.01, 0.02)
        N = random.randint(10, 15)

    elif test_type is TestCaseType.LARGE_TIME_STEPS:
        x0 = random.uniform(1, 10)
        k = random.uniform(1, 1.2)
        dt = random.uniform(0.4, 0.5)
        N = random.randint(10, 15)

    elif test_type is TestCaseType.LONG_INTEGRATION:
        x0 = random.uniform(-10, 10)
        k = random.uniform(0.2, 0.5)
        dt = random.uniform(0.2, 0.3)
        N = random.randint(200, 300)

    elif test_type is TestCaseType.NUMERICAL_NOISE:
        x0 = random.uniform(1, 10)
        k = -2.5
        dt = 0.7
        N = random.randint(20, 30)

    elif test_type is TestCaseType.NUMERICAL_OSCILLATIONS:
        x0 = random.uniform(1, 10)
        k = -2.5
        dt = 0.8
        N = random.randint(20, 30)

    elif test_type is TestCaseType.NUMERICAL_INSTABILITY:
        x0 = random.uniform(1, 10)
        k = -2.5
        dt = 0.9
        N = random.randint(30, 40)

    else:
        raise ValueError(f"Unrecognized test case: {test_type}")

    test_case.input["x0"] = x0
    test_case.input["k"] = k
    test_case.input["dt"] = dt
    test_case.input["N"] = N
    test_case.output["x"] = exponential_growth(x0, k, dt, N)

    return test_case
