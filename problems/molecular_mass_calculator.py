import logging
from typing import Tuple

from numpy.random import choice

from problems.test_case import TestCase, TestCaseTypeEnum, test_case_solution_correct

logger = logging.getLogger(__name__)


class TestCaseType(TestCaseTypeEnum):
    RUST = ('Rust (ferric oxide)', 1)
    PLUTONIUM = ('Plutonium', 1)
    LSD = ('LSD', 1)
    HIGH_T_SUPERCONDUCTOR = ('BSCCO (high temperature superconductor)', 1)
    RANDOM_CHEMICAL = ('random chemical', 2)


class ProblemTestCase(TestCase):
    def input_tuple(self) -> tuple:
        return self.input['chemical_formula'],

    def output_tuple(self) -> tuple:
        return self.output['mass'],

    def output_str(self) -> str:
        return str(self.output['mass'])


FUNCTION_NAME = "molecular_mass"
STATIC_RESOURCES = ["periodic_table.csv"]

INPUT_VARS = ['chemical_formula']
OUTPUT_VARS = ['mass']

PHYSICAL_CONSTANTS = {}

ATOL = {}
RTOL = {
    'mass': 0.1
}


def generate_test_case(test_type: TestCaseType) -> ProblemTestCase:
    test_case = ProblemTestCase(test_type)

    if test_type is TestCaseType.RUST:
        chemical_formula = 'Fe2O3'
    elif test_type is TestCaseType.PLUTONIUM:
        chemical_formula = 'Pu'
    elif test_type is TestCaseType.HIGH_T_SUPERCONDUCTOR:
        chemical_formula = 'Bi2Sr2Ca2Cu3O10'
    elif test_type is TestCaseType.LSD:
        chemical_formula = 'C20H25N3O'
    elif test_type is TestCaseType.RANDOM_CHEMICAL:
        chemical_formula = choice(['CO2', 'CH4', 'C6H12O6', 'PuCoGa5', 'CH3NH2', 'W', 'C2H5OH'], 1)[0]
    else:
        raise ValueError

    test_case.input['chemical_formula'] = chemical_formula
    return test_case


def solve_test_case(test_case: ProblemTestCase) -> None:
    from problems.solutions.molecular_mass_calculator import molecular_mass
    chemical_formula = test_case.input['chemical_formula']
    test_case.output['mass'] = molecular_mass(chemical_formula)


def verify_user_solution(user_input: tuple, user_output: tuple) -> Tuple[bool, str]:
    user_test_case = ProblemTestCase(None, INPUT_VARS, user_input, OUTPUT_VARS, user_output)
    passed, correct_test_case = test_case_solution_correct(user_test_case, ATOL, RTOL, ProblemTestCase, solve_test_case)
    return passed, correct_test_case.output_str()
