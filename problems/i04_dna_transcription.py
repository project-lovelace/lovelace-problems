# ProblemI4.py
# RNA Transcription

import logging
import random

from problems.test_case import TestCase, TestCaseTypeEnum

logger = logging.getLogger(__name__)


class TestCase4Type(TestCaseTypeEnum):
    SHORT_TRNA = ('tRNA-SeC-TCA-2-1', 1)
    INSULIN = ('Insulin [Homo sapiens (human)]', 1)
    RANDOM = ('Randomly generated DNA sequence', 1)


class TestCase4(TestCase):
    def input_tuple(self) -> str:
        return (self.input['dna_str'],)

    def output_tuple(self) -> str:
        return (self.output['rna_str'],)


TEST_CASE_TYPE_ENUM = TestCase4Type
TEST_CASE_CLASS = TestCase4

RESOURCES = []

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


def generate_test_case(test_type: TestCase4Type) -> TestCase4:
    test_case = TestCase4(test_type)

    if test_type == TestCase4Type.RANDOM:
        dna_length = random.randint(5, 100)
        dna_str = generate_dna_sequence(dna_length)
    elif test_type == TestCase4Type.SHORT_TRNA:
        dna_str = 'CTCGGATGATCCTCAGTGGTCTGGGGTGCAGGCTTCAAACCTGTAGCTGTCTAGTGACAGAGTGGTTCAATTCCACCTTTGTAGG'
    elif test_type == TestCase4Type.INSULIN:
        dna_str = 'GAGAGCCACTGCATGCTGGGCCTGGCCGGCGTTGGCACCTGTGGGCACCCAGAGAGCGTGGAGAGAGCTGGGAGGGGCTCACAACAGTGCCGGGAAGTGGGGCTTGGCCCAGGGCCCCCAAGACACACAGACGGCACAGCAGGGCTGGTTCAAGGGCTTTATTCCATCTCTCTCGGTGCAGGAGGCGGCGGGTGTGGGGCTGCCTGCGGGCTGCGTCTAGTTGCAGTAGTTCTCCAGCTGGTAGAGGGAGCAGATGCTGGTACAGCATTGTTCCACAATGCCACGCTTCTGCAGGGACCCCTCCAGGGCCAAGGGCTGCAGGCTGCCTGCACCAGGGCCCCCGCCCAGCTCCACCTGCCCCACTGCCAGGACGTGCCGCGCAGAGCAGGTTCCGGAACAGCGGCGAGGCAGAGGGACACAGGAGGACACAGTCAGGGAGACACAGTGCCCGCCTGCCCGCCAGCCCTAGGTCGCACTCCCACCCATCTCCAGCCGGGCTGGACCCAGGTTAGAGGGAGGGTCACCCACACTGGGTGTGGACCTACAGGCCCCAACGCCCACATGTCCCACCTCCTTCCCCCGCCCCGGGGCAGCGTCACAGTGGGAGCCTGAACAGGTGATCCCAGTACTTCTCCCCAGGGCCTGTCCCCAGCATCTTCCCCATCTCCTGACTATGGAGCTGCCGTGAGGCCTGGCGACAGGGGTCTGGCCCACTCAGGCAGGCAGCCACGCCCTCCTCCGGGCGTGATGGGGTGTTCGCCCAGAGGCAGGCAGCGTGGGGCACCCTGTGACCCCAGGTCACCCAGGACTTTACTTAACAAAACACTTGAATCTGCGGTCATCAAATGAGGGTGGAGAAATGGGCTGCGGGGCATTTGTTTGAGGGGCGAGTGGAGGGAGGAGCGTGCCCACCCTCTGATGTATCTCGGGGCTGCCGAAGCCAACACCGTCCTCAGGCTGAGATTCTGACTGGGCCACAGGGAGCTGGTCACTTTTAGGACGTGACCAAGAGAACTTCTTTTTAAAAAAGTGCACCTGACCCCCTGCTGGGTGGCAGCCTCCTGCCCCCTTCTGCCCATGCTGGGTGGGAGCGCCAGGAGCAGGGGGTGGCTGGGGGCGGCCAGGGGCAGCAATGGGCAGTTGGCTCACCCTGCAGGTCCTCTGCCTCCCGGCGGGTCTTGGGTGTGTAGAAGAAGCCTCGTTCCCCGCACACTAGGTAGAGAGCTTCCACCAGGTGTGAGCCGCACAGGTGTTGGTTCACAAAGGCTGCGGCTGGGTCAGGTCCCCAGAGGGCCAGCAGCGCCAGCAGGGGCAGGAGGCGCATCCACAGGGCCATGGCAGAAGGACAGTGATCTGGGAGACAGGCAGGGCTGAGGCAGGCTGAAGGCCAGGTGCCCTGCCTTGGGGCCCCTGGGCTCACCCCCACATGCTTCACGAGCCCAGCCACGTCCTCCCTGCTGCAGAGCTGGGGCCTGGGGTCCAGCCACCCTGGAATCCTGAGCCCACCTGACGCAAAGGCCCTTGGAACAGACCTGCTTGATGGCCTCTTCTGATGCAGCCTGTCCTGGAGGGCTGAGGGCTGCTGGGCCCCCGCTGGCTTTATAGTCTCAGAGCCCATCTCCCCTACCTCTCAACCCCTGCCGCCTGGCCCATTAGGGCCTGGGGTGGGGGGGTCGGCAGATGGCTGGGGGCTGAGGCTGCAATTTCCGGACCATTT'
    else:
        raise Exception('Shitty code')

    test_case.input['dna_str'] = dna_str
    return test_case


def solve_test_case(test_case: TestCase4) -> None:
    dna_str = test_case.input['dna_str']
    test_case.output['rna_str'] = dna_complement(dna_str)
    return


def verify_user_solution(user_input: tuple, user_output: tuple) -> bool:
    logger.info("Verifying user solution...")
    logger.debug("User input: %s", user_input)
    logger.debug("User output: %s", user_output)

    # Build TestCase object out of user's input string.
    tmp_test_case = TestCase4()

    dna_str = user_input[0]
    tmp_test_case.input = {'dna_str': dna_str}

    # Solve the problem with this TestCase so we have our own solution, and extract the solution.
    solve_test_case(tmp_test_case)
    rna_str = tmp_test_case.output['rna_str']

    # Extract user solution.
    user_rna_str = user_output[0]

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
