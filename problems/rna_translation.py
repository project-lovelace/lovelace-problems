import random
import logging

from problems.test_case import TestCase, TestCaseTypeEnum
from problems.solutions.rna_translation import amino_acid_sequence, rna_codon_table

logger = logging.getLogger(__name__)

FUNCTION_NAME = "amino_acid_sequence"

INPUT_VARS = ["rna"]
OUTPUT_VARS = ["amino_acid_sequence"]

STATIC_RESOURCES = []

PHYSICAL_CONSTANTS = {}
ATOL = {}
RTOL = {}

class ProblemTestCase(TestCase):
    def input_tuple(self):
        return self.input["rna"],

    def output_tuple(self):
        return self.output["amino_acid_sequence"],

class TestCaseType(TestCaseTypeEnum):
    NO_CODONS = ("No codons", 1)
    ONE_CODON = ("One codon", 5)
    FEW_CODONS = ("Few codons", 2)
    MANY_CODONS = ("Many codons", 2)
    ALL_CODONS = ("All codons", 1)
    END_CODON = ("End codon", 2)
    STOP_IN_MIDDLE = ("Stop codon in the middle", 1)

start_codons = ["AUG"]
stop_codons = ["UAA", "UAG", "UGA"]

intermediate_codon_table = rna_codon_table.copy()
[intermediate_codon_table.pop(codon) for codon in start_codons + stop_codons]

def random_codons(N):
    return "".join(["".join(random.choices("ACGU", k=3)) for _ in range(N)])

def random_intermediate_codons(N):
    return "".join(random.choices(list(intermediate_codon_table.keys()), k=N))

def generate_test_case(test_type):
    test_case = ProblemTestCase(test_type)

    if test_type is TestCaseType.NO_CODONS:
        rna = ""

    elif test_type is TestCaseType.ONE_CODON:
        rna = random_intermediate_codons(1)

    elif test_type is TestCaseType.FEW_CODONS:
        N = random.randint(2, 5)
        rna = random_intermediate_codons(N) + random.choice(stop_codons)

    elif test_type is TestCaseType.MANY_CODONS:
        N = random.randint(10, 100)
        rna = random_intermediate_codons(N)

    elif test_type is TestCaseType.ALL_CODONS:
        rna = start_codons[0] + "".join(list(intermediate_codon_table.keys())) + random.choice(stop_codons)

    elif test_type is TestCaseType.END_CODON:
        rna = random.choice(stop_codons)

    elif test_type is TestCaseType.STOP_IN_MIDDLE:
        N1 = random.randint(10, 20)
        N2 = random.randint(5, 10)
        rna = random_intermediate_codons(N1) + random.choice(stop_codons) + random_intermediate_codons(N2)

    else:
        raise ValueError(f"Unrecognized test case: {test_type}")

    test_case.input["rna"] = rna
    test_case.output["amino_acid_sequence"] = amino_acid_sequence(rna)

    return test_case
