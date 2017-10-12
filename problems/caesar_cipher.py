import random
import string

from problems.test_case import TestCase, TestCaseTypeEnum

from os import path
import logging, logging.config

logging_config_path = path.join(path.dirname(path.abspath(__file__)), '..', 'logging.ini')
logging.config.fileConfig(logging_config_path)
logger = logging.getLogger(__name__)


class TestCaseI5Type(TestCaseTypeEnum):
    RANDOM_STRING = ('random string', '', 1)
    UNKNOWN = ('unknown case', 0)


class TestCaseI5(TestCase):
    def input_str(self) -> str:
        return ' '.join(self.input['colors'])

    def output_str(self) -> str:
        pass


TEST_CASE_TYPE_ENUM = TestCaseI5Type
TEST_CASE_CLASS = TestCaseI5

PHYSICAL_CONSTANTS = {}
TESTING_CONSTANTS = {}


def generate_random_string(length):
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(length))


def randomly_insert_spaces(s):
    length = len(s)
    n = random.randint(int(length/10), int(length/4))
    for _ in range(n):
        pos = random.randint(0, length-1)
        s = s[:pos] + ' ' + s[pos:]
    return s


def caesar_cipher(plaintext, shift):
    alphabet = string.ascii_uppercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted_alphabet)
    return plaintext.translate(table)


def generate_input(test_type: TestCaseI5Type) -> TestCaseI5:
    test_case = TestCaseI5(test_type)

    if test_type is TestCaseI5Type.RANDOM_STRING:
        length = random.randint(50, 400)
        plaintext = randomly_insert_spaces(generate_random_string(length))

    known_word = random.choice(plaintext.split())

    shift = random.randint(1, 25)
    ciphertext = caesar_cipher(plaintext, shift)

    test_case.input['ciphertext'] = ciphertext
    test_case.input['known_word'] = known_word
    return test_case


def solve_test_case(test_case: TestCaseI5) -> None:
    # WARNING: UNTESTED!
    ciphertext = test_case.input['ciphertext']
    known_word = test_case.input['known_word']

    for shift in range(len(string.ascii_uppercase)):
        if known_word in caesar_cipher(ciphertext, shift).split():
            decrypted_message = caesar_cipher(ciphertext, shift)
            break

    test_case.output['decrypted_message'] = decrypted_message
    return


def verify_user_solution(user_input_str: str, user_output_str: str) -> bool:
    logger.info("Verifying user solution...")
    logger.debug("User input string: %s", user_input_str)
    logger.debug("User output string: %s", user_output_str)

    # Build TestCase object out of user's input string.
    tmp_test_case = TestCaseI5(TestCaseI5Type.UNKNOWN)

    ciphertext = user_input_str
    tmp_test_case.input = {'ciphertext': ciphertext}

    # Solve the problem with this TestCase so we have our own solution, and extract the solution.
    solve_test_case(tmp_test_case)
    decrypted_message = tmp_test_case.output['decrypted_message']

    # Extract user solution.
    user_decrypted_message = user_output_str

    logger.debug("User solution:")
    logger.debug("decrypted_message = %s", user_decrypted_message)
    logger.debug("Engine solution:")
    logger.debug("decrypted message = %s", decrypted_message)

    if user_decrypted_message == decrypted_message
        logger.info("User solution correct.")
        return True
    else:
        logger.info("User solution incorrect.")
        return False