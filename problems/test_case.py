import logging
from enum import Enum
from math import isclose
from typing import Tuple

from numpy import ndarray, array_equal, allclose

logger = logging.getLogger(__name__)


class TestCaseMismatchError(Exception):
    pass


class TestCaseTypeEnum(Enum):
    def __init__(self, test_name, multiplicity):
        self.test_name = test_name
        self.multiplicity = multiplicity


class TestCase(object):
    def __init__(self, test_type=None, input_vars=None, input_tuple=None, output_vars=None, output_tuple=None):
        self.test_type = test_type

        self.input = {}
        if input_vars is not None and input_tuple is not None:
            if len(input_vars) != len(input_tuple):
                raise ValueError("input_vars and input_tuple must be of the same length but input_vars={:} (len={:d}), "
                                 "input_tuple={:} (len={:d})".format(input_vars, len(input_vars),
                                                                     input_tuple, len(input_tuple)))
            for var, val in zip(input_vars, input_tuple):
                self.input[var] = val

        self.output = {}
        if output_vars is not None and output_tuple is not None:
            if len(output_vars) != len(output_tuple):
                raise ValueError("output_vars and output_tuple must be of the same length but output_vars={:} "
                                 "(len={:d}), output_tuple={:} (len={:d})".format(output_vars, len(output_vars),
                                                                                  output_tuple, len(output_tuple)))
            for var, val in zip(output_vars, output_tuple):
                self.output[var] = val

    def input_tuple(self) -> tuple:
        pass

    def output_tuple(self) -> tuple:
        pass


def values_match(v1, v2, tt, tol) -> bool:
    """
    Check if v1 and v2 are equal. For ints and floats, an absolute or relative tolerance can be specified.
    Lists and tuples are checked recursively.

    :param v1: One value.
    :param v2: Another value.
    :param tt: Tolerance type: None, "absolute", or "relative".
    :param tol: Tolerance value if using "absolute" or "relative".
    :return: True or False
    """
    if isinstance(v1, (list, ndarray)) and isinstance(v2, (list, ndarray)):
        if tt is None:
            return array_equal(v1, v2)
        elif tt == "absolute":
            return allclose(v1, v2, atol=tol)
        elif tt == "relative":
            return allclose(v1, v2, rtol=tol)

    # Values can't match if they're of different types. But if they're ints or floats, that's fine.
    if not isinstance(v1, (int, float)) and not isinstance(v2, (int, float)) and type(v1) != type(v2):
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


def test_case_solution_correct(correct_test_case: TestCase, user_test_case: TestCase, atol: dict, rtol: dict) -> Tuple[bool, TestCase]:
    """
    Check whether user_test_case contains the correct output. Absolute and relative tolerances can be specified via
    the atol and rtol dictionaries.

    :param user_test_case: A TestCase object containing input given to the user and the output they produced.
    :param atol: A dictionary of absolute tolerances.
    :param rtol: A dictionary of relative tolerances.
    :param problem_test_case: A function that can be used to construct TestCase objects.
    :param solve_test_case: A function that can be used to fill the test case output with the correct output.
    :return: True or False, and a TestCase containing the correct output.
    """
    logger.info("Verifying user solution for test case {:}...".format(correct_test_case.test_type))

    input_vars = list(user_test_case.input.keys())
    output_vars = list(user_test_case.output.keys())

    for i, var in enumerate(input_vars):
        var_type = type(user_test_case.input[var])
        val = user_test_case.input[var]
        logger.debug("Test case input {:d}: name={:s}, type={:}, value={:}".format(i, var, var_type, val))

    # Assume user output is false until we can check that all values match.
    test_case_passed = False
    values_passed = []

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

        values_passed.append(output_correct)
        if output_correct is False:
            logger.info("User output for {:s} is wrong.".format(var))
        else:
            logger.info("User output for {:s} is correct.".format(var))

    if all(values_passed):
        test_case_passed = True

    return test_case_passed, correct_test_case
