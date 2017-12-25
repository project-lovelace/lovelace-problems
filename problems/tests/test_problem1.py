import pytest

from .. import earthquake_epicenters as problem


def test_general_case():
    test_case_type_enum = problem.TEST_CASE_TYPE_ENUM
    tc = problem.generate_input(test_case_type_enum.GENERAL)
    problem.solve_test_case(tc)
    assert problem.verify_user_solution(tc.input_str(), tc.output_str())


def test_zero_case():
    test_case_type_enum = problem.TEST_CASE_TYPE_ENUM
    tc = problem.generate_input(test_case_type_enum.ZERO_CASE)
    problem.solve_test_case(tc)
    assert problem.verify_user_solution(tc.input_str(), tc.output_str())


def test_equidistant_case():
    test_case_type_enum = problem.TEST_CASE_TYPE_ENUM
    tc = problem.generate_input(test_case_type_enum.EQUIDISTANT)
    problem.solve_test_case(tc)
    assert problem.verify_user_solution(tc.input_str(), tc.output_str())


def test_raises_exception_on_not_enum():
    with pytest.raises(TypeError):
        problem.generate_input(6969)
