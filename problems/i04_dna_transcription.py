# ProblemI4.py
# RNA Transcription

import logging
import random
from problems.test_case import TestCase, TestCaseTypeEnum

logger = logging.getLogger(__name__)


class TestCaseI4Type(TestCaseTypeEnum):
    RANDOM = ('Randomly generated DNA sequence', '', 5)
    UNKNOWN = ('unknown case', '', 0)


class TestCaseI4(TestCase):
    def input_str(self) -> str:
        return str(self.input['dna_str'])

    def output_str(self) -> str:
        return self.output['rna_str']


TEST_CASE_TYPE_ENUM = TestCaseI4Type
TEST_CASE_CLASS = TestCaseI4

PHYSICAL_CONSTANTS = {}
TESTING_CONSTANTS = {}


def generate_dna_sequence(length):
    return ''.join(random.choice('ATGC') for _ in range(length))


def randomly_insert_extra_sites(sequence, n):
    # Insert the string "CCWGG" (W = A or T) at n random locations of the
    # string sequence.
    # TODO: Does this run in O(n)?
    length = len(sequence)
    for _ in range(length):
        site = 'CC' + random.choice('AT') + 'GG'
        pos = random.randint(0, length-1)
        sequence = sequence[:pos] + site + sequence[pos:]
    return sequence


def dna_complement(seq):
    base_pairs = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    complement = [base_pairs[base] for base in list(seq)]
    return ''.join(complement)


def generate_input(test_type: TestCaseI4Type) -> TestCaseI4:
    test_case = TestCaseI4(test_type)

    if test_type == TestCaseI4Type.RANDOM:
        dna_length = random.randint(5, 100)
        dna_str = generate_dna_sequence(dna_length)
    else:
        raise Exception('Shitty code')

    test_case.input['dna_str'] = dna_str
    return test_case


def solve_test_case(test_case: TestCaseI4) -> None:
    dna_str = test_case.input['dna_str']
    test_case.output['rna_str'] = dna_complement(dna_str)
    return


def verify_user_solution(user_input_str: str, user_output_str: str) -> bool:
    logger.info("Verifying user solution...")
    logger.debug("User input string: %s", user_input_str)
    logger.debug("User output string: %s", user_output_str)

    # Build TestCase object out of user's input string.
    tmp_test_case = TestCaseI4(TestCaseI4Type.UNKNOWN)

    dna_str = user_input_str
    tmp_test_case.input = {'dna_str': dna_str}

    # Solve the problem with this TestCase so we have our own solution, and extract the solution.
    solve_test_case(tmp_test_case)
    rna_str = tmp_test_case.output['rna_str']

    # Extract user solution.
    user_rna_str = user_output_str

    logger.debug("User solution:")
    logger.debug("rna_str = %s", user_rna_str)
    logger.debug("Engine solution:")
    logger.debug("rna_str = %s", rna_str)

    if rna_str == user_rna_str:
        logger.info("User solution correct.")
        return True
    else:
        logger.info("User solution incorrect.")
        return False
