import logging

from problems.test_case import TestCase, TestCaseTypeEnum

logger = logging.getLogger(__name__)


class TestCase10Type(TestCaseTypeEnum):
    STILL_LIFE = ('still life', 1)
    OSCILLATORS = ('oscillators', 1)
    SPACESHIPS = ('spaceships', 1)


class TestCase10(TestCase):
    def input_tuple(self) -> tuple:
        return (self.input['board_filename'].split('/')[1], self.input['steps'])

    def output_tuple(self) -> str:
        return (self.output['board_str'],)


TEST_CASE_TYPE_ENUM = TestCase10Type
TEST_CASE_CLASS = TestCase10

STATIC_RESOURCES = ['still_life.txt', 'oscillators.txt', 'spaceships.txt']

PHYSICAL_CONSTANTS = {}
TESTING_CONSTANTS = {}


def generate_test_case(test_type: TestCase10Type) -> TestCase10:
    test_case = TestCase10(test_type)

    if test_type is TestCase10Type.STILL_LIFE:
        board_filename = 'i10_game_of_life/still_life.txt'
    elif test_type is TestCase10Type.OSCILLATORS:
        board_filename = 'i10_game_of_life/oscillators.txt'
    elif test_type is TestCase10Type.SPACESHIPS:
        board_filename = 'i10_game_of_life/spaceships.txt'
    else:
        raise ValueError

    test_case.input['board_filename'] = board_filename
    test_case.input['steps'] = 15
    test_case.input['USER_GENERATED_FILES'] = ['board.txt']
    return test_case


# Game of life functions

def neighbors(cell, distance=1):
    x, y = cell
    r = range(0 - distance, 1 + distance)
    return ((x + i, y + j)         # new cell offset from center
            for i in r for j in r  # iterate over range in 2d
            if not i == j == 0)    # exclude the center cell


def advance(board):
    new_board = set()
    for cell in board:
        cell_neighbors = set(neighbors(cell))

        # test if live cell dies
        if len(board & cell_neighbors) in [2, 3]:
            new_board.add(cell)

        # test dead neighbors to see if alive
        for n in cell_neighbors:
            if len(board & set(neighbors(n))) is 3:
                new_board.add(n)

    return new_board


def constrain(board, size):
    return set(cell for cell in board if cell[0] <= size and cell[1] <= size)


def solve_test_case(test_case: TestCase10) -> None:
    board_filename = test_case.input['board_filename']
    steps = test_case.input['steps']

    board = set()

    i = 0
    j = 0
    i_max = 0
    j_max = 0

    with open(board_filename) as board_file:
        for line in board_file.readlines():
            if j > j_max:
                j_max = j
            j = 0
            for c in line:
                if c == 'o':
                    board.add((i, j))
                j = j + 1
            if i > i_max:
                i_max = i
            i = i + 1

    size = max(i_max, j_max)

    for i in range(1, steps+1):
        board = constrain(advance(board), size)

    sizex = sizey = size or 0
    for x, y in board:
        sizex = x if x > sizex else sizex
        sizey = y if y > sizey else sizey

    board_str = ''
    for i in range(sizex + 1):
        for j in range(sizey + 1):
            char = 'o' if (i, j) in board else '.'
            board_str = board_str + char
        board_str = board_str + '\n'

    test_case.output['board_str'] = board_str
    return


def verify_user_solution(user_input: tuple, user_output: tuple) -> bool:
    logger.info("Verifying user solution...")
    logger.debug("User input: %s", user_input)
    logger.debug("User output: %s", user_output)

    # Build TestCase object out of user's input string.
    tmp_test_case = TestCase10()
    tmp_test_case.input['board_filename'] = user_input[0]
    tmp_test_case.input['steps'] = user_input[1]

    # Solve the problem with this TestCase so we have our own solution, and extract the solution.
    solve_test_case(tmp_test_case)
    board_str = tmp_test_case.output['board_str']

    # Extract user solution.
    with open('board.txt') as board_file:
        user_board_str = board_file.read()

    logger.debug("User solution:")
    logger.debug("{:s}".format(user_board_str))
    logger.debug("Engine solution:")
    logger.debug("{:s}".format(board_str))

    user_solution_correct = True
    for i in range(len(board_str)):
        if board_str[i] != user_board_str[i]:
            user_solution_correct = False
            break

    if user_solution_correct:
        logger.info("User solution correct.")
        return True
    else:
        logger.info("User solution incorrect.")
        return False
