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


board_filename = input()
steps = int(input())

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
            j = j+1
        if i > i_max:
            i_max = i
        i = i+1

size = max(i_max, j_max)

for i in range(1, steps + 1):
    # sys.stdout.write('\033[H')  # move to the top
    # sys.stdout.write('\033[J')  # clear the screen
    # print('step:', i, '/', steps)
    # print_board(board, size)
    # time.sleep(0.2)
    board = constrain(advance(board), size)

# print_board(board, size)
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

with open("board.txt", "w") as f:
    f.write('{:s}'.format(board_str))