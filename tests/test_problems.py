import logging
import pkgutil
import importlib
import pytest
import problems

from types import ModuleType

log = logging.getLogger(__name__)

problem_modules = pkgutil.iter_modules(problems.__path__)
problem_names = [m.name for m in problem_modules]

# test_case.py is not a problem module
problem_names = list(filter(lambda s: "test_case" not in s, problem_names))

@pytest.mark.parametrize("problem_name", problem_names)
def test_importing_problem_module(problem_name):
    problem_module = importlib.import_module("problems." + problem_name)
    assert isinstance(problem_module, ModuleType)

@pytest.mark.parametrize("problem_name", problem_names)
def test_function_name_exists(problem_name):
    problem_module = importlib.import_module("problems." + problem_name)
    assert isinstance(problem_module.FUNCTION_NAME, str)

@pytest.mark.parametrize("problem_name", problem_names)
def test_input_output_vars(problem_name):
    problem_module = importlib.import_module("problems." + problem_name)
    assert isinstance(problem_module.INPUT_VARS, list)
    assert isinstance(problem_module.OUTPUT_VARS, list)

@pytest.mark.parametrize("problem_name", problem_names)
def test_problem_parameters(problem_name):
    problem_module = importlib.import_module("problems." + problem_name)
    assert isinstance(problem_module.STATIC_RESOURCES, list)
    assert isinstance(problem_module.PHYSICAL_CONSTANTS, dict)
    assert isinstance(problem_module.ATOL, dict)
    assert isinstance(problem_module.RTOL, dict)

@pytest.mark.parametrize("problem_name", problem_names)
def test_problem_test_case_types(problem_name):
    problem_module = importlib.import_module("problems." + problem_name)
    assert len(problem_module.TestCaseType) > 0
    for test_case_type in problem_module.TestCaseType:
        assert isinstance(test_case_type.test_name, str)
        assert isinstance(test_case_type.multiplicity, int)

@pytest.mark.parametrize("problem_name", problem_names)
def test_problem_test_case_generation(problem_name):

    problem_module = importlib.import_module("problems." + problem_name)
    assert len(problem_module.TestCaseType) > 0

    if len(problem_module.STATIC_RESOURCES) > 0:
        log.info(f"Skipping problem {problem_name} as we can't test problems with static resources yet.")
        return True

    for test_case_type in problem_module.TestCaseType:

        if test_case_type.multiplicity == 0:
            # These are usually disabled or not yet implemented tests.
            log.info(f"Skipping problem {problem_name} test case type {test_case_type} with multiplicity 0.")
            continue

        test_case = problem_module.generate_test_case(test_case_type)

        assert test_case.test_type == test_case_type
        assert isinstance(test_case.input, dict)
        assert isinstance(test_case.output, dict)

        for input_name, input_value in test_case.input.items():
            assert isinstance(input_name, str)
            assert input_name in problem_module.INPUT_VARS

        for output_name, output_value in test_case.output.items():
            assert isinstance(output_name, str)
            assert output_name in problem_module.OUTPUT_VARS

        input_tuple = test_case.input_tuple()
        assert len(input_tuple) == len(problem_module.INPUT_VARS)
        for input_name, input_value in zip(problem_module.INPUT_VARS, input_tuple):
            assert test_case.input[input_name] == input_value

        output_tuple = test_case.output_tuple()
        assert len(output_tuple) == len(problem_module.OUTPUT_VARS)
        for output_name, output_value in zip(problem_module.OUTPUT_VARS, output_tuple):
            assert test_case.output[output_name] == output_value
