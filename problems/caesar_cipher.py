import string
import random
import logging
from typing import Tuple

from problems.test_case import TestCase, TestCaseTypeEnum, test_case_solution_correct
from problems.solutions.caesar_cipher import break_caesar_cipher

logger = logging.getLogger(__name__)

FUNCTION_NAME = "break_caesar_cipher"
INPUT_VARS = ['ciphertext', 'known_word']
OUTPUT_VARS = ['decrypted_message']

STATIC_RESOURCES = []

PHYSICAL_CONSTANTS = {}
ATOL = {}
RTOL = {}


class TestCaseType(TestCaseTypeEnum):
    MOBY_DICK = ('Moby dick', 1)
    THE_WIRE = ('Bunny Colvin (The Wire)', 1)
    RANDOM_STRING = ('random string', 1)


class ProblemTestCase(TestCase):
    def input_tuple(self) -> tuple:
        return self.input['ciphertext'], self.input['known_word']

    def output_tuple(self) -> tuple:
        return self.output['decrypted_message'],

    def output_str(self) -> str:
        return self.output['decrypted_message']


def generate_random_string(length):
    return "".join(random.choice(string.ascii_lowercase) for _ in range(length))


def randomly_insert_spaces(s):
    length = len(s)
    n = random.randint(int(length/10), int(length/4))
    for _ in range(n):
        pos = random.randint(0, length-1)
        s = s[:pos] + " " + s[pos:]
    return s


def caesar_cipher(plaintext, shift):
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted_alphabet)
    return plaintext.translate(table)


def generate_test_case(test_type: TestCaseType) -> ProblemTestCase:
    test_case = ProblemTestCase(test_type)

    if test_type is TestCaseType.RANDOM_STRING:
        length = random.randint(50, 400)
        plaintext = randomly_insert_spaces(generate_random_string(length))

    elif test_type is TestCaseType.MOBY_DICK:
        plaintext = "Call me Ishmael Some years ago never mind how long precisely having little or no money in my purse and nothing particular to interest me on shore I thought I would sail about a little and see the watery part of the world".lower()

    elif test_type is TestCaseType.THE_WIRE:
        plaintext = "This drug thing this aint police work I mean I can send any fool with a badge and a gun to a corner to jack a crew and grab vials But policing I mean you call something a war and pretty soon everyone is going to be running around acting like warriors They gonna be running around on a damn crusade storming corners racking up body counts And when you at war you need a fucking enemy And pretty soon damn near everybody on every corner is your fucking enemy And soon, the neighborhood youre supposed to be policing thats just occupied territory".lower()

    known_word = random.choice(plaintext.split())

    shift = random.randint(1, 25)
    ciphertext = caesar_cipher(plaintext, shift).upper()

    test_case.input['ciphertext'] = ciphertext
    test_case.input['known_word'] = known_word
    test_case.output['decrypted_message'] = break_caesar_cipher(ciphertext, known_word)

    return test_case


def verify_user_solution(correct_test_case: TestCase, user_input: tuple, user_output: tuple) -> Tuple[bool, str]:
    user_test_case = ProblemTestCase(None, INPUT_VARS, user_input, OUTPUT_VARS, user_output)
    passed, correct_test_case = test_case_solution_correct(correct_test_case, user_test_case, ATOL, RTOL)
    return passed, correct_test_case.output_str()
