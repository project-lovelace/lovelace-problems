import logging
from typing import Tuple

from numpy import array, zeros, reshape
from numpy.random import randint, choice

from problems.test_case import TestCase, TestCaseTypeEnum, test_case_solution_correct
from problems.solutions.game_of_life import game_of_life

logger = logging.getLogger(__name__)

FUNCTION_NAME = "game_of_life"
INPUT_VARS = ['board', 'steps']
OUTPUT_VARS = ['board']

STATIC_RESOURCES = ["still_life.txt", "oscillators.txt", "spaceships.txt"]

PHYSICAL_CONSTANTS = {}
ATOL = {}
RTOL = {}

ALIVE = 1
DEAD = 0

# Still life patterns
BLOCK = reshape(array(list("1111"), dtype=int), (2, 2))
BEEHIVE = reshape(array(list("011010010110"), dtype=int), (3, 4))
LOAF = reshape(array(list("0110100101010010"), dtype=int), (4, 4))
BOAT = reshape(array(list("110101010"), dtype=int), (3, 3))
TUB = reshape(array(list("010101010"), dtype=int), (3, 3))

# Oscillator patterns
BLINKER = reshape(array(list("111"), dtype=int), (1, 3))
TOAD = reshape(array(list("01111110"), dtype=int), (2, 4))
BEACON = reshape(array(list("1100110000110011"), dtype=int), (4, 4))

PULSAR_STR = "0011100011100" + 13*"0" + 3*"1000010100001" + "0011100011100" + 13*"0" + "0011100011100" + 3*"1000010100001" + 13*"0" + "0011100011100"
PULSAR = reshape(array(list(PULSAR_STR), dtype=int), (13, 13))

# Infinite growth patterns
GLIDER_GUN_STR = 24*"0" + "1" + 11*"0" + \
                 22*"0" + "101" + 11*"0" + \
                 12*"0" + "11" + 6*"0" + "11" + 12*"0" + "11" + \
                 11*"0" + "10001000011" + 12*"0" + "11" + \
                 "11" + 8*"0" + "100000100011" + 14*"0" + \
                 "11" + 8*"0" + "100010110000101" + 11*"0" + \
                 10*"0" + "100000100000001" + 11*"0" + \
                 11*"0" + "10001" + 20*"0" + \
                 12*"0" + "11" + 22*"0"
GLIDER_GUN = reshape(array(list(GLIDER_GUN_STR), dtype=int), (9, 36))


class TestCaseType(TestCaseTypeEnum):
    STILL_LIFE = ("still life", 1)
    OSCILLATORS = ("oscillators", 1)
    GLIDERS = ("gliders", 0)
    GLIDER_GUN = ("glider gun", 1)
    RANDOM_SMALL = ("small random", 1)
    RANDOM_LARGE = ("large random", 0)


class ProblemTestCase(TestCase):
    def input_tuple(self) -> tuple:
        return self.input['board'], self.input['steps']

    def output_tuple(self) -> tuple:
        return self.output['board'],

    def output_str(self) -> str:
        return str(self.output['board'])


def generate_test_case(test_type: TestCaseType) -> ProblemTestCase:
    test_case = ProblemTestCase(test_type)

    if test_type is TestCaseType.STILL_LIFE:
        grid = zeros((15, 15), dtype=int)
        steps = 5
        grid[1:3, 1:3] = BLOCK
        grid[5:8, 2:6] = BEEHIVE
        grid[1:5, 7:11] = LOAF
        grid[6:9, 10:13] = TUB

    elif test_type is TestCaseType.OSCILLATORS:
        grid = zeros((17, 36), dtype=int)
        steps = 31
        grid[3, 16:19] = BLINKER
        grid[8:10, 15:19] = TOAD
        grid[10:14, 1:5] = BEACON
        grid[2:15, 21:34] = PULSAR

    elif test_type is TestCaseType.GLIDERS:
        raise NotImplementedError

    elif test_type is TestCaseType.GLIDER_GUN:
        N = randint(15, 50)
        M = randint(50, 100)
        steps = 10
        grid = zeros((N, M), dtype=int)
        grid[2:11, 2:38] = GLIDER_GUN

    elif test_type is TestCaseType.RANDOM_SMALL:
        N = randint(5, 50)
        M = randint(5, 50)
        steps = randint(3, 10)
        grid = choice([ALIVE, DEAD], N*M, p=[0.5, 0.5]).reshape(N, M)

    elif test_type is TestCaseType.RANDOM_LARGE:
        N = randint(200, 250)
        M = randint(200, 250)
        steps = randint(3, 10)
        grid = choice([ALIVE, DEAD], N*M, p=[0.5, 0.5]).reshape(N, M)

    test_case.input["board"] = grid.tolist()
    test_case.input["steps"] = steps
    test_case.output["board"] = game_of_life(grid, steps)

    return test_case


def verify_user_solution(correct_test_case: TestCase, user_input: tuple, user_output: tuple) -> Tuple[bool, str]:
    user_test_case = ProblemTestCase(None, INPUT_VARS, user_input, OUTPUT_VARS, user_output)
    passed, correct_test_case = test_case_solution_correct(correct_test_case, user_test_case, ATOL, RTOL)
    return passed, correct_test_case.output_str()
