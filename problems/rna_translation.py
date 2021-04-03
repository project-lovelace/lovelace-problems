import random
import logging

from problems.test_case import TestCase, TestCaseTypeEnum
from problems.solutions.rna_translation import amino_acid_sequence

logger = logging.getLogger(__name__)

FUNCTION_NAME = "amino_acid_sequence"

INPUT_VARS = ["rna"]
OUTPUT_VARS = ["amino_acid_sequence"]

STATIC_RESOURCES = []

PHYSICAL_CONSTANTS = {}
ATOL = {}
RTOL = {}

class TestCaseType(TestCaseTypeEnum):
    ONE_AMINO_ACID = ("One amino acid", 1)

class ProblemTestCase(TestCase):
    def input_tuple(self):
        return self.input["rna"],

    def output_tuple(self):
        return self.output["amino_acid_sequence"],

def generate_test_case(test_type):
    test_case = ProblemTestCase(test_type)

    if test_type is TestCaseType.ONE_AMINO_ACID:
        rna = "UUU"

    else:
        raise ValueError(f"Unrecognized test case: {test_type}")

    test_case.input["rna"] = rna
    test_case.output["amino_acid_sequence"] = amino_acid_sequence(rna)

    return test_case
