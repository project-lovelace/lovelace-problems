import logging

import numpy as np

from problems.test_case import TestCase, TestCaseTypeEnum

logger = logging.getLogger(__name__)


class TestCaseI8Type(TestCaseTypeEnum):
    RUST = ('Rust (ferric oxide)', '', 1)
    PLUTONIIM = ('Plutonium', '', 1)
    LSD = ('LSD', '', 1)
    HIGH_T_SUPERCONDUCTOR = ('BSCCO (high temperature superconductor)', '', 1)
    RANDOM_CHEMICAL = ('random chemical', '', 2)
    UNKNOWN = ('unknown case', '', 0)


class TestCaseI8(TestCase):
    def input_str(self) -> str:
        return self.input['chemical_formula']

    def output_str(self) -> str:
        return float(self.output['mass'])


TEST_CASE_TYPE_ENUM = TestCaseI8Type
TEST_CASE_CLASS = TestCaseI8

RESOURCES = ['periodic_table.csv']

PHYSICAL_CONSTANTS = {}

TESTING_CONSTANTS = {
    'error_tol': 0.1  # tolerance on each resistance output [Ohm]
}


def generate_input(test_type: TestCaseI8Type) -> TestCaseI8:
    test_case = TestCaseI8(test_type)

    if test_type is TestCaseI8Type.RUST:
        chemical_formula = 'Fe2O3'
    elif test_type is TestCaseI8Type.PLUTONIUM:
        chemical_formula = 'Pu'
    elif test_type is TestCaseI8Type.ACETONE:
        chemical_formula = 'CH3COCH3'
    elif test_type is TestCaseI8Type.HIGH_T_SUPERCONDUCTOR:
        chemical_formula = 'Bi2Sr2Ca2Cu3O10'
    elif test_type is TestCaseI8Type.LSD:
        chemical_formula = 'C20H25N3O'
    elif test_type is TestCaseI8Type.RANDOM_CHEMICAL:
        chemical_formula = np.random.choice(['CO2', 'CH4', 'C6H12O6', 'PuCoGa5', 'CH3NH2', 'W', 'C2H5OH'], 1)[0]
    else:
        raise ValueError

    test_case.input['chemical_formula'] = chemical_formula
    return test_case


def solve_test_case(test_case: TestCaseI8) -> None:
    import csv
    import re

    atomic_masses = {}
    with open('periodic_table.csv') as csvfile:
        ptable_reader = csv.reader(csvfile, delimiter=',')
        for row in ptable_reader:
            element_symbol = str(row[0])
            atomic_mass = float(row[1])
            atomic_masses[element_symbol] = atomic_mass

    chemical_formula = test_case.input['chemical_formula']

    pattern = re.compile(r'([A-Z][a-z]?)([0-9]*)')
    mass = 0
    for symbol, number in re.findall(pattern, chemical_formula):
        if not number:
            number = 1
        mass = mass + int(number) * atomic_masses[symbol]

    test_case.output['mass'] = mass
    return


def verify_user_solution(user_input_str: str, user_output_str: str) -> bool:
    logger.info("Verifying user solution...")
    logger.debug("User input string: %s", user_input_str)
    logger.debug("User output string: %s", user_output_str)

    # Build TestCase object out of user's input string.
    tmp_test_case = TestCaseI8(TestCaseI8Type.UNKNOWN)

    inputs = user_input_str.split()
    chemical_formula = inputs[0]
    tmp_test_case.input = {'chemical_formula': chemical_formula}

    # Solve the problem with this TestCase so we have our own solution, and extract the solution.
    solve_test_case(tmp_test_case)
    mass = tmp_test_case.output['mass']

    # Extract user solution.
    user_mass = float(user_output_str)

    error_tol = TESTING_CONSTANTS['error_tol']
    error_mass = abs(mass - user_mass)

    logger.debug("User solution:")
    logger.debug("mass = {}".format(user_mass))
    logger.debug("Engine solution:")
    logger.debug("mass = {}".format(mass))
    logger.debug("Error tolerance = %e. Error mass: %e.", error_tol, error_mass)

    if error_mass < error_tol:
        logger.info("User solution correct.")
        return True
    else:
        logger.info("User solution incorrect.")
        return False
