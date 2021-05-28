board = {}

for row in range(0, 7):
    for column in range(0, 7):
        coordinate = (int(row), int(column))
        board[coordinate] = 'X'

# set white marble initial positions
board[0, 0] = 'W'
board[0, 1] = 'W'
board[1, 0] = 'W'
board[1, 1] = 'W'

board[5, 5] = 'W'
board[5, 6] = 'W'
board[6, 5] = 'W'
board[6, 6] = 'W'

# set black marble initial positions
board[0, 5] = 'B'
board[0, 6] = 'B'
board[1, 5] = 'B'
board[1, 6] = 'B'

board[5, 0] = 'B'
board[5, 1] = 'B'
board[6, 0] = 'B'
board[6, 1] = 'B'

# set red marble initial positions
board[1, 3] = 'R'
board[2, 2] = 'R'
board[2, 3] = 'R'
board[2, 4] = 'R'
board[3, 1] = 'R'
board[3, 2] = 'R'
board[3, 3] = 'R'
board[3, 4] = 'R'
board[3, 5] = 'R'
board[4, 2] = 'R'
board[4, 3] = 'R'
board[4, 4] = 'R'
board[5, 3] = 'R'

print(board)