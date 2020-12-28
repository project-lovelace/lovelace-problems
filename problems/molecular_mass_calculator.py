import logging
from typing import Tuple

from numpy.random import choice

from problems.test_case import TestCase, TestCaseTypeEnum

logger = logging.getLogger(__name__)

FUNCTION_NAME = "molecular_mass"
INPUT_VARS = ['chemical_formula']
OUTPUT_VARS = ['mass']

STATIC_RESOURCES = ["periodic_table.csv"]

PHYSICAL_CONSTANTS = {}
ATOL = {}
RTOL = {
    'mass': 0.1
}


class TestCaseType(TestCaseTypeEnum):
    RUST = ("Rust (ferric oxide)", 1)
    PLUTONIUM = ("Plutonium", 1)
    LSD = ("LSD", 1)
    HIGH_T_SUPERCONDUCTOR = ("BSCCO (high temperature superconductor)", 1)
    RANDOM_CHEMICAL = ("random chemical", 2)


class ProblemTestCase(TestCase):
    def input_tuple(self) -> tuple:
        return self.input['chemical_formula'],

    def output_tuple(self) -> tuple:
        return self.output['mass'],

    def output_str(self) -> str:
        return str(self.output['mass'])


def generate_test_case(test_type: TestCaseType) -> ProblemTestCase:
    test_case = ProblemTestCase(test_type)

    if test_type is TestCaseType.RUST:
        chemical_formula = "Fe2O3"

    elif test_type is TestCaseType.PLUTONIUM:
        chemical_formula = "Pu"

    elif test_type is TestCaseType.HIGH_T_SUPERCONDUCTOR:
        chemical_formula = "Bi2Sr2Ca2Cu3O10"

    elif test_type is TestCaseType.LSD:
        chemical_formula = "C20H25N3O"

    elif test_type is TestCaseType.RANDOM_CHEMICAL:
        chemical_formula = choice(["CO2", "CH4", "C6H12O6", "PuCoGa5", "CH3NH2", "W", "C2H5OH"], 1)[0]

    test_case.input['chemical_formula'] = chemical_formula

    from problems.solutions.molecular_mass_calculator import molecular_mass
    test_case.output['mass'] = molecular_mass(chemical_formula)

    return test_case
