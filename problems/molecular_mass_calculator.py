import logging

import numpy as np

from problems.test_case import TestCase, TestCaseTypeEnum

logger = logging.getLogger(__name__)


class TestCaseType(TestCaseTypeEnum):
    RUST = ('Rust (ferric oxide)', 1)
    PLUTONIUM = ('Plutonium', 1)
    LSD = ('LSD', 1)
    HIGH_T_SUPERCONDUCTOR = ('BSCCO (high temperature superconductor)', 1)
    RANDOM_CHEMICAL = ('random chemical', 2)


class ProblemTestCase(TestCase):
    def input_tuple(self) -> tuple:
        return (self.input['chemical_formula'],)

    def output_tuple(self) -> tuple:
        return (self.output['mass'],)


TEST_CASE_TYPE_ENUM = TestCaseType
TEST_CASE_CLASS = ProblemTestCase
FUNCTION_NAME = "molecular_mass"
STATIC_RESOURCES = ['periodic_table.csv']

PHYSICAL_CONSTANTS = {}

TESTING_CONSTANTS = {
    'error_tol': 0.1  # tolerance on each resistance output [Ohm]
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
        chemical_formula = np.random.choice(['CO2', 'CH4', 'C6H12O6', 'PuCoGa5', 'CH3NH2', 'W', 'C2H5OH'], 1)[0]
    else:
        raise ValueError

    test_case.input['chemical_formula'] = chemical_formula
    return test_case


def solve_test_case(test_case: ProblemTestCase) -> None:
    from problems.solutions.molecular_mass_calculator import molecular_mass
    chemical_formula = test_case.input['chemical_formula']
    test_case.output['mass'] = molecular_mass(chemical_formula)
    return


def verify_user_solution(user_input: tuple, user_output: tuple) -> bool:
    logger.info("Verifying user solution...")
    logger.debug("User input: %s", user_input)
    logger.debug("User output: %s", user_output)

    # Build TestCase object out of user's input string.
    tmp_test_case = ProblemTestCase()

    chemical_formula = user_input[0]
    tmp_test_case.input = {'chemical_formula': chemical_formula}

    # Solve the problem with this TestCase so we have our own solution, and extract the solution.
    solve_test_case(tmp_test_case)
    mass = tmp_test_case.output['mass']

    # Extract user solution.
    user_mass = user_output[0]

    error_tol = TESTING_CONSTANTS['error_tol']
    error_mass = abs(mass - user_mass)

    logger.debug("User solution:")
    logger.debug("mass = {}".format(user_mass))
    logger.debug("Engine solution:")
    logger.debug("mass = {}".format(mass))
    logger.debug("Error tolerance = %e. Error mass: %e.", error_tol, error_mass)

    passed = False

    if error_mass < error_tol:
        logger.info("User solution correct within error tolerance of {:g}.".format(error_tol))
        passed = True
    else:
        logger.info("User solution incorrect.")

    return passed, str(mass)
