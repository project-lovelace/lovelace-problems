import math
import logging

from numpy import mean, var
from numpy.random import randint, uniform

from problems.test_case import TestCase, TestCaseTypeEnum

logger = logging.getLogger(__name__)


class TestCaseType(TestCaseTypeEnum):
    RANDOM_SMALL = ("Random (small)", 1)
    RANDOM_LARGE = ("Random (large)", 1)


class ProblemTestCase(TestCase):
    def input_tuple(self) -> tuple:
        return (self.input["temperatures"],)

    def output_tuple(self) -> tuple:
        return (self.output["T_avg"], self.output["T_var"])


FUNCTION_NAME = "temperature_statistics"
STATIC_RESOURCES = []

PHYSICAL_CONSTANTS = {}
TESTING_CONSTANTS = {
    "rel_tol": 1e-8
}


def generate_test_case(test_type: TestCaseType) -> ProblemTestCase:
    test_case = ProblemTestCase(test_type)

    if test_type is TestCaseType.RANDOM_SMALL:
        n = randint(5, 15)
        Ts = uniform(-20, 35, size=n)
    elif test_type is TestCaseType.SUN_TO_EARTH:
        n = randint(1000, 2000)
        Ts = uniform(-20, 35, size=n)
    else:
        raise ValueError("Invalid test case type.")

    test_case.input["temperatures"] = Ts

    return test_case


def solve_test_case(test_case: ProblemTestCase) -> None:
    T = test_case.input["temperatures"]
    test_case.output["T_avg"] = mean(T)
    test_case.output["T_var"] = var(T)
    return


def verify_user_solution(user_input: tuple, user_output: tuple) -> bool:
    logger.info("Verifying user solution...")
    logger.debug("User input tuple: %s", user_input)
    logger.debug("User output tuple: %s", user_output)

    tmp_test_case = ProblemTestCase()

    Ts = user_input[0]
    tmp_test_case.input = {"temperatures": Ts}

    solve_test_case(tmp_test_case)
    T_avg = tmp_test_case.output["T_avg"]
    T_var = tmp_test_case.output["T_var"]

    user_T_avg = user_output[0]
    user_T_var = user_output[1]

    rtol = TESTING_CONSTANTS["rel_tol"]

    logger.debug("User solution:")
    logger.debug("T_avg = {:f}".format(user_T_avg))
    logger.debug("T_var = {:f}".format(user_T_var))
    logger.debug("Engine solution:")
    logger.debug("T_avg = {:f}".format(T_avg))
    logger.debug("T_var = {:f}".format(T_var))
    logger.debug("Relative tolerance = {:g}.".format(rtol))

    passed = False

    if math.isclose(T_avg, user_T_avg, rel_tol=rtol) and math.isclose(T_var, user_T_var, rel_tol=rtol):
        logger.info("User solution correct.")
        passed = True
    else:
        logger.info("User solution is wrong.")
        passed = False

    return passed, "T_avg = {:f}, T_var = {:f}".format(T_avg, T_var)
