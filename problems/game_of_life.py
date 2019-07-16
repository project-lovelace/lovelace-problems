import logging

import numpy as np

from problems.test_case import TestCase, TestCaseTypeEnum
from problems.solutions.game_of_life import game_of_life

logger = logging.getLogger(__name__)


class TestCaseType(TestCaseTypeEnum):
    STILL_LIFE = ("still life", 1)
    OSCILLATORS = ("oscillators", 1)
    GLIDERS = ("gliders", 0)
    GLIDER_GUN = ("glider gun", 1)
    RANDOM_SMALL = ("small random", 1)
    RANDOM_LARGE = ("large random", 0)
    RANDOM_LONG = ("long random", 0)


class ProblemTestCase(TestCase):
    def input_tuple(self) -> tuple:
        return (self.input["board"],self.input["steps"])

    def output_tuple(self) -> tuple:
        return (self.output["board"],)


TEST_CASE_TYPE_ENUM = TestCaseType
TEST_CASE_CLASS = ProblemTestCase
FUNCTION_NAME = "game_of_life"
STATIC_RESOURCES = ['still_life.txt', 'oscillators.txt', 'spaceships.txt']

PHYSICAL_CONSTANTS = {}
TESTING_CONSTANTS = {}

ALIVE = 1
DEAD = 0

# Still life patterns
BLOCK = np.reshape(np.array(list("1111"), dtype=int), (2, 2))
BEEHIVE = np.reshape(np.array(list("011010010110"), dtype=int), (3, 4))
LOAF = np.reshape(np.array(list("0110100101010010"), dtype=int), (4, 4))
BOAT = np.reshape(np.array(list("110101010"), dtype=int), (3, 3))
TUB = np.reshape(np.array(list("010101010"), dtype=int), (3, 3))

# Oscillator patterns
BLINKER = np.reshape(np.array(list("111"), dtype=int), (1, 3))
TOAD = np.reshape(np.array(list("01111110"), dtype=int), (2, 4))
BEACON = np.reshape(np.array(list("1100110000110011"), dtype=int), (4, 4))

PULSAR_STR = "0011100011100" + 13*"0" + 3*"1000010100001" + "0011100011100" + 13*"0" + "0011100011100" + 3*"1000010100001" + 13*"0" + "0011100011100"
PULSAR = np.reshape(np.array(list(PULSAR_STR), dtype=int), (13, 13))

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
GLIDER_GUN = np.reshape(np.array(list(GLIDER_GUN_STR), dtype=int), (9, 36))


def generate_test_case(test_type: TestCaseType) -> ProblemTestCase:
    test_case = ProblemTestCase(test_type)

    if test_type is TestCaseType.STILL_LIFE:
        grid = np.zeros((15, 15), dtype=int)
        steps = 5
        grid[1:3, 1:3] = BLOCK
        grid[5:8, 2:6] = BEEHIVE
        grid[1:5, 7:11] = LOAF
        grid[6:9, 10:13] = TUB
    elif test_type is TestCaseType.OSCILLATORS:
        grid = np.zeros((17, 36), dtype=int)
        steps = 30
        grid[3, 16:19] = BLINKER
        grid[8:10, 15:19] = TOAD
        grid[10:14, 1:5] = BEACON
        grid[2:15, 21:34] = PULSAR
    elif test_type is TestCaseType.GLIDERS:
        raise NotImplementedError
    elif test_type is TestCaseType.GLIDER_GUN:
        N = np.random.randint(15, 50)
        M = np.random.randint(50, 100)
        steps = 200
        grid = np.zeros((N, M), dtype=int)
        grid[2:11, 2:38] = GLIDER_GUN
    elif test_type is TestCaseType.RANDOM_SMALL:
        N = np.random.randint(5, 50)
        M = np.random.randint(5, 50)
        steps = np.random.randint(1, 100)
        grid = np.random.choice([ALIVE, DEAD], N*M, p=[0.5, 0.5]).reshape(N, M)
    elif test_type is TestCaseType.RANDOM_LARGE:
        N = np.random.randint(200, 250)
        M = np.random.randint(200, 250)
        steps = np.random.randint(50, 100)
        grid = np.random.choice([ALIVE, DEAD], N*M, p=[0.5, 0.5]).reshape(N, M)
    elif test_type is TestCaseType.RANDOM_LONG:
        N, M = 50, 50
        steps = 1000
        grid = np.random.choice([ALIVE, DEAD], N*M, p=[0.5, 0.5]).reshape(N, M)
    else:
        raise ValueError

    test_case.input["board"] = grid.tolist()
    test_case.input["steps"] = steps
    return test_case


def solve_test_case(test_case: ProblemTestCase) -> None:
    grid = test_case.input["board"]
    steps = test_case.input["steps"]
    test_case.output["board"] = game_of_life(grid, steps)
    return


def verify_user_solution(user_input: tuple, user_output: tuple) -> bool:
    logger.info("Verifying user solution...")
    logger.debug("User input: %s", user_input)
    logger.debug("User output: %s", user_output)

    # Build TestCase object out of user's input string.
    tmp_test_case = ProblemTestCase()
    tmp_test_case.input["board"] = user_input[0]
    tmp_test_case.input["steps"] = user_input[1]

    # Solve the problem with this TestCase so we have our own solution, and extract the solution.
    solve_test_case(tmp_test_case)
    end_board = tmp_test_case.output["board"]

    user_end_board = user_output[0]

    logger.debug("User solution:")
    logger.debug("{:}".format(user_end_board))
    logger.debug("Engine solution:")
    logger.debug("{:}".format(end_board))

    user_solution_correct = True if np.array_equal(user_end_board, end_board) else False

    passed = False

    if user_solution_correct:
        logger.info("User solution correct.")
        passed = True
    else:
        logger.info("User solution incorrect.")

    return passed, str(end_board)
