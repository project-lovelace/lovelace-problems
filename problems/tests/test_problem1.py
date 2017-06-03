import pytest

from .. import problem1 as problem


def test_all_problem1_test_cases():
    test_case_type_enum = problem.TEST_CASE_TYPE_ENUM

    test_cases = []
    for test_type in test_case_type_enum:
        for _ in range(test_type.multiplicity):
            test_cases.append(problem.generate_input(test_type))

    for tc in test_cases:
        problem.solve_test_case(tc)
        assert problem.verify_user_solution(tc.input_str(), tc.output_str())
