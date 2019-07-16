import logging
from enum import Enum
from math import isclose

logger = logging.getLogger(__name__)


class TestCaseMismatchError(Exception):
    pass


class TestCaseTypeEnum(Enum):
    def __init__(self, test_name, multiplicity):
        self.test_name = test_name
        self.multiplicity = multiplicity


class TestCase(object):    
    def __init__(self, test_type=None):
        self.test_type = test_type
        self.input = {}
        self.output = {}

    def input_tuple(self) -> tuple:
        pass

    def output_tuple(self) -> tuple:
        pass


def values_match(v1, v2, tt, tol) -> bool:
    if type(v1) != type(v2):
        logger.debug("v1 and v2 types do not match: v1_type={:}, v2_type={:}".format(type(v1), type(v2)))
        return False

    if isinstance(v1, (list, tuple)):
        if len(v1) != len(v2):
            logger.debug("v1 and v2 lengths do not match: v1_len={:d}, v2_len={:d}".format(len(v1), len(v2)))
            return False

        for e1, e2 in zip(v1, v2):
            # Recursively check that each element of the two lists or tuples match.
            if values_match(e1, e2, tt, tol) is False:
                return False

        # We've gone through the entire list/tuple and each pair of elements match, so return True.
        return True

    if isinstance(v1, (int, float)):
        if tt is None:
            return v1 == v2
        elif tt == "absolute":
            return isclose(v1, v2, abs_tol=tol)
        elif tt == "relative":
            return isclose(v1, v2, rel_tol=tol)
    else:
        return v1 == v2  # Takes care of strings (and hopefully other data types).


def test_case_solution_correct(user_test_case: TestCase, atol: dict, rtol: dict, problem_test_case, solve_test_case) -> tuple:
    logger.info("Verifying user solution...")

    input_vars = list(user_test_case.input.keys())

    for i, var in enumerate(input_vars):
        var_type = type(user_test_case.input[var])
        val = user_test_case.input[var]
        logger.debug("Test case input {:d}: name={:s}, type={:}, value={:}".format(i, var, var_type, val))

    # Create empty test case that we'll fill with the correct input and output.
    correct_test_case = problem_test_case()

    # Fill empty test case with the inputs the user was given.
    for var in input_vars:
        correct_test_case.input[var] = user_test_case.input[var]

    # Now that the test case has inputs, solve it to fill the outputs with the correct solution.
    solve_test_case(correct_test_case)

    output_vars = list(user_test_case.output.keys())

    # Assume user output is correct until we find a mismatching value.
    test_case_passed = True

    # Verify that every output matches.
    for i, var in enumerate(output_vars):
        var_type = type(user_test_case.output[var])
        user_val = user_test_case.output[var]
        correct_val = correct_test_case.output[var]

        # Raise an error if both an absolute and relative tolerance are defined. Technically non-fatal as we could just
        # pick one, but this should encourage less sloppy problem modules.
        if var in atol.keys() and var in rtol.keys():
            raise TestCaseMismatchError("Both atol={:} and rtol={:} are defined for output var {:s}! "
                                        "Only one must be defined.""".format(atol[var], rtol[var], var))

        if var in atol.keys():
            tolerance_type, tolerance = "absolute", atol[var]
        elif var in rtol.keys():
            tolerance_type, tolerance = "relative", rtol[var]
        else:
            tolerance_type, tolerance = None, 0

        logger.debug("Test case output {:d}: name={:s}, type={:}, user_value={:}, correct_value={:}, "
                     "tolerance_type={:}, tolerance={:}".format(i, var, var_type, user_val, correct_val,
                                                                tolerance_type, tolerance))

        output_correct = values_match(user_val, correct_val, tolerance_type, tolerance)

        if output_correct is False:
            test_case_passed = False
            logger.info("User output for {:s} is wrong.".format(var))
        else:
            logger.info("User output for {:s} is correct.".format(var))

    return test_case_passed, correct_test_case
