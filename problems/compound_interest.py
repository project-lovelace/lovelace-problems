import logging

from numpy.random import uniform, randint

from problems.test_case import TestCase, TestCaseTypeEnum
from problems.solutions.compound_interest import compound_interest

logger = logging.getLogger(__name__)

FUNCTION_NAME = "compound_interest"
INPUT_VARS = ["amount", "rate", "years"]
OUTPUT_VARS = ["new_amount"]

STATIC_RESOURCES = []
PHYSICAL_CONSTANTS = {}

ATOL = {}
RTOL = {
    "new_amount": 1e-6
}


class TestCaseType(TestCaseTypeEnum):
    NO_INTEREST = ("No interest", 1)
    SAVINGS = ("High-rate savings account", 1)
    SP_500 = ("S&P 500 average annual return", 1)
    CREDIT_CARD = ("Credit card debt", 1)
    RANDOM = ("Random", 2)


class ProblemTestCase(TestCase):
    def input_tuple(self):
        return self.input["amount"], self.input["rate"], self.input["years"]

    def output_tuple(self):
        return self.output["new_amount"],


def generate_test_case(test_type):
    test_case = ProblemTestCase(test_type)

    if test_type is TestCaseType.NO_INTEREST:
        amount = uniform(10, 1000)
        rate = 0.0
        years = randint(1, 10)

    if test_type is TestCaseType.SAVINGS:
        amount = uniform(100, 25000)
        rate = 0.005
        years = randint(10, 25)

    if test_type is TestCaseType.SP_500:
        amount = uniform(10000, 500000)
        rate = 0.1
        years = randint(7, 30)

    if test_type is TestCaseType.CREDIT_CARD:
        amount = uniform(250, 10000)
        rate = 0.1
        years = randint(7, 30)

    if test_type is TestCaseType.RANDOM:
        amount = uniform(0, 100000)
        rate = uniform(0, 0.25)
        years = randint(0, 30)

    else:
        raise ValueError(f"Unrecognized test case: {test_type}")

    test_case.input["amount"] = amount
    test_case.input["rate"] = rate
    test_case.input["years"] = years
    test_case.output["new_amount"] = compound_interest(amount, rate, years)

    return test_case
