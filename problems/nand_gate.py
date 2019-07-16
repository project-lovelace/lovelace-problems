import logging

from problems.test_case import TestCase, TestCaseTypeEnum

logger = logging.getLogger(__name__)
from problems.solutions.nand_gate import NAND


class TestCaseType(TestCaseTypeEnum):
    ZERO_ZERO = ("00", 1)
    ZERO_ONE = ("01", 1)
    ONE_ZERO = ("10", 1)
    ONE_ONE = ("11", 1)


class ProblemTestCase(TestCase):
    def input_tuple(self) -> tuple:
        return self.input["p"], self.input["q"]

    def output_tuple(self) -> tuple:
        return (self.output["nand"],)


TEST_CASE_TYPE_ENUM = TestCaseType
TEST_CASE_CLASS = ProblemTestCase
FUNCTION_NAME = "NAND"
STATIC_RESOURCES = []

PHYSICAL_CONSTANTS = {}
TESTING_CONSTANTS = {}


def generate_test_case(test_type: TestCaseType) -> ProblemTestCase:
    test_case = ProblemTestCase(test_type)

    if test_type is TestCaseType.ZERO_ZERO:
        p, q = 0, 0
    elif test_type is TestCaseType.ZERO_ONE:
        p, q = 0, 1
    elif test_type is TestCaseType.ONE_ZERO:
        p, q = 1, 0
    elif test_type is TestCaseType.ONE_ONE:
        p, q = 1, 1
    else:
        raise ValueError("Invalid test case type.")

    test_case.input["p"], test_case.input["q"] = p, q

    return test_case


def solve_test_case(test_case: ProblemTestCase) -> None:
    p = test_case.input["p"]
    q = test_case.input["q"]
    test_case.output["nand"] = NAND(p, q)
    return


def verify_user_solution(user_input: tuple, user_output: tuple) -> bool:
    logger.info("Verifying user solution...")
    logger.debug("User input tuple: %s", user_input)
    logger.debug("User output tuple: %s", user_output)

    tmp_test_case = ProblemTestCase()

    p, q = user_input
    tmp_test_case.input = {"p": p, "q": q}

    solve_test_case(tmp_test_case)
    nand = tmp_test_case.output["nand"]

    user_nand = user_output[0]

    logger.debug("User solution:")
    logger.debug("nand = {:d}".format(user_nand))
    logger.debug("Engine solution:")
    logger.debug("nand = {:d}".format(nand))

    passed = False

    if user_nand == nand:
        logger.info("User solution correct.")
        passed = True
    else:
        logger.info("User solution is wrong.")

    return passed, str(nand)
