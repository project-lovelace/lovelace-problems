import random
import logging

from problems.test_case import TestCase, TestCaseTypeEnum

logger = logging.getLogger(__name__)


class TestCaseType(TestCaseTypeEnum):
    NO_DONATIONS = ("No donations have been made.", 1)
    LUCKY_PATIENT = ("Lucky patient (O- is available)", 1)
    LUCKY_ABP_PATIENT = ("Lucky AB+ patient", 1)
    SLIM_PICKINGS = ("Slim pickings (few donations)", 2)
    WELL_STOCKED = ("Well stocked hospital (many donations)", 2)


class ProblemTestCase(TestCase):
    def input_tuple(self) -> tuple:
        return self.input["patient_blood_type"], self.input["donated_blood"]

    def output_tuple(self) -> tuple:
        return (self.output["survive"],)


TEST_CASE_TYPE_ENUM = TestCaseType
TEST_CASE_CLASS = ProblemTestCase
FUNCTION_NAME = "survive"
STATIC_RESOURCES = []

PHYSICAL_CONSTANTS = {
    "blood_types": ["A-", "B-", "AB-", "O-", "A+", "B+", "AB+", "O+"]
}
TESTING_CONSTANTS = {}


def generate_test_case(test_type: TestCaseType) -> ProblemTestCase:
    test_case = ProblemTestCase(test_type)
    blood_types = PHYSICAL_CONSTANTS["blood_types"]

    if test_type is TestCaseType.NO_DONATIONS:
        patient_blood_type = random.choice(blood_types)
        donated_blood = []
    elif test_type is TestCaseType.LUCKY_PATIENT:
        patient_blood_type = random.choice(blood_types)
        donated_blood = ["O-", "O-", "O-"]
    elif test_type is TestCaseType.LUCKY_ABP_PATIENT:
        patient_blood_type = "AB+"
        donated_blood = random.choice(blood_types)
    elif test_type is TestCaseType.SLIM_PICKINGS:
        patient_blood_type = random.choice(blood_types)
        donated_blood = random.choices(blood_types, k=random.randint(2, 3))
    elif test_type is TestCaseType.WELL_STOCKED:
        patient_blood_type = random.choice(blood_types)
        donated_blood = random.choices(blood_types, k=random.randint(8, 25))
    else:
        raise ValueError("Invalid test case type.")

    test_case.input = {
        "patient_blood_type": patient_blood_type,
        "donated_blood": donated_blood
    }

    return test_case


def solve_test_case(test_case: ProblemTestCase) -> None:
    def survive(patient_blood_type, donated_blood):
        if len(donated_blood) == 0:
            return False

        b = patient_blood_type

        if b == "AB+" or "O-" in donated_blood:
            return True

        if b == "A+":
            if "A+" in donated_blood or "A-" in donated_blood or "O+" in donated_blood:
                return True

        if b == "O+":
            if "O+" in donated_blood:
                return True

        if b == "B+":
            if "B+" in donated_blood or "B-" in donated_blood or "O+" in donated_blood:
                return True

        if b == "A-":
            if "A-" in donated_blood:
                return True

        if b == "O-":
            if "O-" in donated_blood:
                return True

        if b == "B-":
            if "B-" in donated_blood:
                return True

        if b == "AB-":
            if "AB-" in donated_blood or "A-" in donated_blood or "B-" in donated_blood:
                return True

        return False

    b = test_case.input["patient_blood_type"]
    donated_blood = test_case.input["donated_blood"]
    test_case.output["survive"] = survive(b, donated_blood)
    return


def verify_user_solution(user_input: tuple, user_output: tuple) -> bool:
    logger.info("Verifying user solution...")
    logger.debug("User input tuple: %s", user_input)
    logger.debug("User output tuple: %s", user_output)

    tmp_test_case = ProblemTestCase()

    patient_blood_type, donated_blood = user_input

    tmp_test_case.input = {
        "patient_blood_type": patient_blood_type,
        "donated_blood": donated_blood
    }

    solve_test_case(tmp_test_case)
    survive = tmp_test_case.output["survive"]

    user_survive = user_output[0]

    logger.debug("User solution:")
    logger.debug("survive = {:}".format(user_survive))
    logger.debug("Engine solution:")
    logger.debug("survive = {:}".format(survive))

    passed = False

    if survive == user_survive:
        logger.info("User solution correct.")
        passed = True
    else:
        logger.info("User solution is wrong.")
        passed = False

    return passed, str(survive)
