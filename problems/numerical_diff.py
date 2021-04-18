import logging
from math import exp, sin
from random import uniform

from problems.test_case import TestCase, TestCaseTypeEnum
from problems.solutions.numerical_diff import numerical_diff

logger = logging.getLogger(__name__)

FUNCTION_NAME = "numerical_diff"
INPUT_VARS = ['f', 'x']
OUTPUT_VARS = ['df']

STATIC_RESOURCES = []

PHYSICAL_CONSTANTS = {}
ATOL = {}
RTOL = {
    'df': 0.005,  # 0.5% relative tolerance
}


class TestCaseType(TestCaseTypeEnum):
    ZERO = ("Zero function", 1)
    CONSTANT = ("Constant function", 1)
    LINEAR = ("Linear polynomial", 1)
    QUADRATIC = ("Quadratic polynomial", 1)
    CUBIC = ("Cubic polynomial", 1)
    SINE = ("Sine function", 1)
    EXPONENTIAL = ("Exponential function", 1)


class ProblemTestCase(TestCase):
    def input_tuple(self) -> tuple:
        return self.input['f', 'x'],

    def output_tuple(self) -> tuple:
        return self.output['df'],


def generate_test_case(test_type: TestCaseType) -> ProblemTestCase:
    test_case = ProblemTestCase(test_type)

    x = uniform(-10, 10)
    
    if test_type is TestCaseType.ZERO:
        f = lambda x: 0
        
    elif test_type is TestCaseType.CONSTANT:
        f = lambda x: 2021
    
    elif test_type is TestCaseType.LINEAR:
        f = lambda x: 2021*x + 3
        
    elif test_type is TestCaseType.QUADRATIC:
        f = lambda x: x**2 + 2*x
    
    elif test_type is TestCaseType.CUBIC:
        f = lambda x: 3*x**3
        
    elif test_type is TestCaseType.SINE:
        f = sin
        
    elif test_type is TestCaseType.EXPONENTIAL:
        f = exp

    else:
        raise ValueError(f"Unrecognized test case: {test_type}")

    test_case.input = {
        'f': f,
        'x': x,
    }
    
    test_case.output['df'] = numerical_diff(f, x)

    return test_case