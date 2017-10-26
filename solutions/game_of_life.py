board = set()
steps = int(input())

with open('initial_board.txt') as board_file:
    for line in board_file.readlines():
        board.append(map(lambda s: True if s == 'o' else False, list(line)))

for _ in range(steps):
    for i in len(board):
        for j in len(board[i]):
            if board[i][j]:
