import logging
from random import choice, choices, randint
from typing import Tuple

from problems.test_case import TestCase, TestCaseTypeEnum, test_case_solution_correct
from problems.solutions.blood_types import survive

logger = logging.getLogger(__name__)

FUNCTION_NAME = "survive"
INPUT_VARS = ["patient_blood_type", "donated_blood"]
OUTPUT_VARS = ["survive"]

STATIC_RESOURCES = []

PHYSICAL_CONSTANTS = {"blood_types": ["A-", "B-", "AB-", "O-", "A+", "B+", "AB+", "O+"]}

ATOL = {}
RTOL = {}


class TestCaseType(TestCaseTypeEnum):
    NO_DONATIONS = ("No donations have been made.", 0)
    LUCKY_PATIENT = ("Lucky patient (O- is available)", 1)
    LUCKY_ABP_PATIENT = ("Lucky AB+ patient", 1)
    SLIM_PICKINGS = ("Slim pickings (few donations)", 2)
    WELL_STOCKED = ("Well stocked hospital (many donations)", 2)
    UNLUCKY_ONEG_PATIENT = ("Unlucky O- patient (No suitable donors available)", 1)
    UNLUCKY_OPOS_PATIENT = ("Unlucky O+ patient (No suitable donors available)", 1)
    UNLUCKY_ANEG_PATIENT = ("Unlucky A- patient (No suitable donors available)", 1)
    UNLUCKY_APOS_PATIENT = ("Unlucky A+ patient (No suitable donors available)", 1)
    UNLUCKY_BNEG_PATIENT = ("Unlucky B- patient (No suitable donors available)", 1)
    UNLUCKY_BPOS_PATIENT = ("Unlucky B+ patient (No suitable donors available)", 1)
    UNLUCKY_ABNEG_PATIENT = ("Unlucky AB- patient (No suitable donors available)", 1)
    UNLUCKY_ABPOS_PATIENT = ("Unlucky AB+ patient (No suitable donors available)", 1)


class ProblemTestCase(TestCase):
    def input_tuple(self) -> tuple:
        return self.input["patient_blood_type"], self.input["donated_blood"]

    def output_tuple(self) -> tuple:
        return (self.output["survive"],)

    def output_str(self) -> str:
        return str(self.output["survive"])


def generate_test_case(test_type: TestCaseType) -> ProblemTestCase:
    test_case = ProblemTestCase(test_type)
    blood_types = PHYSICAL_CONSTANTS["blood_types"]

    if test_type is TestCaseType.NO_DONATIONS:
        patient_blood_type = choice(blood_types)
        donated_blood = []

    elif test_type is TestCaseType.LUCKY_PATIENT:
        patient_blood_type = choice(blood_types)
        donated_blood = ["O-", "O-", "O-"]

    elif test_type is TestCaseType.LUCKY_ABP_PATIENT:
        patient_blood_type = "AB+"
        donated_blood = [choice(blood_types)]

    elif test_type is TestCaseType.SLIM_PICKINGS:
        patient_blood_type = choice(blood_types)
        donated_blood = choices(blood_types, k=randint(2, 3))

    elif test_type is TestCaseType.WELL_STOCKED:
        patient_blood_type = choice(blood_types)
        donated_blood = choices(blood_types, k=randint(8, 25))

    elif test_type is TestCaseType.UNLUCKY_ONEG_PATIENT:
        patient_blood_type = "O-"
        donated_blood = ["A-", "B-", "AB-", "A+", "B+", "AB+", "O+"]

    elif test_type is TestCaseType.UNLUCKY_OPOS_PATIENT:
        patient_blood_type = "O+"
        donated_blood = ["A-", "B-", "AB-", "A+", "B+", "AB+"]

    elif test_type is TestCaseType.UNLUCKY_ANEG_PATIENT:
        patient_blood_type = "A-"
        donated_blood = ["B-", "AB-", "A+", "B+", "AB+", "O+"]

    elif test_type is TestCaseType.UNLUCKY_APOS_PATIENT:
        patient_blood_type = "A+"
        donated_blood = ["B-", "AB-", "B+", "AB+"]

    elif test_type is TestCaseType.UNLUCKY_BNEG_PATIENT:
        patient_blood_type = "B-"
        donated_blood = ["A-", "AB-", "A+", "B+", "AB+", "O+"]

    elif test_type is TestCaseType.UNLUCKY_BPOS_PATIENT:
        patient_blood_type = "B+"
        donated_blood = ["A-", "AB-", "A+", "AB+"]

    elif test_type is TestCaseType.UNLUCKY_ABNEG_PATIENT:
        patient_blood_type = "AB-"
        donated_blood = ["A+", "B+", "AB+", "O+"]

    elif test_type is TestCaseType.UNLUCKY_ABPOS_PATIENT:
        patient_blood_type = "AB+"
        donated_blood = []

    else:
        raise ValueError("Unrecognized test case: {}".format(test_type))

    test_case.input = {"patient_blood_type": patient_blood_type, "donated_blood": donated_blood}

    test_case.output["survive"] = survive(patient_blood_type, donated_blood)

    return test_case


def verify_user_solution(correct_test_case: TestCase, user_input: tuple, user_output: tuple) -> Tuple[bool, str]:
    user_test_case = ProblemTestCase(None, INPUT_VARS, user_input, OUTPUT_VARS, user_output)
    passed, correct_test_case = test_case_solution_correct(correct_test_case, user_test_case, ATOL, RTOL)
    return passed, correct_test_case.output_str()
