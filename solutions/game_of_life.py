import sys
import time
import subprocess


def neighbors(cell, distance=1):
    x, y = cell
    r = range(0 - distance, 1 + distance)
    return ((x + i, y + j)         # new cell offset from center
            for i in r for j in r  # iterate over range in 2d
            if not i == j == 0)    # exclude the center cell


def advance(board):
    """Advance the board one step and return it."""
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


def print_board(board, size=None):
    rows, cols = subprocess.check_output(['stty', 'size']).split()
    cols = int(cols)

    sizex = sizey = size or 0
    for x, y in board:
        sizex = x if x > sizex else sizex
        sizey = y if y > sizey else sizey

    for i in range(sizex + 1):
        for j in range(sizey + 1):
            sys.stdout.write('o' if (i, j) in board else '.')
        padding = (cols - sizey - 1) * ' '
        sys.stdout.write(padding)

    sys.stdout.flush()


def constrain(board, size):
    return set(cell for cell in board if cell[0] <= size and cell[1] <= size)


board = set()
steps = int(input())

with open('initial_board.txt') as board_file:
    i = 0
    for line in board_file.readlines():
        j = 0
        for c in line:
            if c == 'o':
                board.add((i, j))
            j = j+1
        i = i+1

steps = 50
size = 30

for i in range(1, steps + 1):
    # sys.stdout.write('\033[H')  # move to the top
    # sys.stdout.write('\033[J')  # clear the screen
    # print('step:', i, '/', steps)
    # print_board(board, size)
    # time.sleep(0.2)
    board = constrain(advance(board), size)

print_board(board, size)