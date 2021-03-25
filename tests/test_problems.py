import pkgutil
import importlib
import pytest
import problems

from types import ModuleType

problem_modules = pkgutil.iter_modules(problems.__path__)
problem_names = [m.name for m in problem_modules]

@pytest.mark.parametrize("problem_name", problem_names)
def test_importing_problem_module(problem_name):
    problem_module = importlib.import_module("problems." + problem_name)
    assert isinstance(problem_module, ModuleType)

@pytest.mark.parametrize("problem_name", problem_names)
def test_function_name_exists(problem_name):
    problem_module = importlib.import_module("problems." + problem_name)
    assert isinstance(problem_module.FUNCTION_NAME, str)
