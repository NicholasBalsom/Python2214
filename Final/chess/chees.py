chessboard = [
    ["R", "N", "B", "Q", "K", "B", "N", "R"],
    ["P", "P", "P", "P", "P", "P", "P", "P"],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    ["p", "p", "p", "p", "p", "p", "p", "p"],
    ["r", "n", "b", "q", "k", "b", "n", "r"]
]

def print_board(board):
    for row in board:
        print(" ".join(row))

# Define a function to get the coordinates of a given piece on the board
def get_piece_location(board, piece):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == piece:
                return (i, j)

# Define a function to make a move on the chessboard
def make_move(board, move):
    # Parse the move into its source and destination squares
    src_col, src_row, dest_col, dest_row = ord(move[0]) - ord('a'), int(move[1]) - 1, ord(move[3]) - ord('a'), int(move[4]) - 1
    # Make the move by updating the board
    board[dest_row][dest_col] = board[src_row][src_col]
    board[src_row][src_col] = "."

#game
player = 1
while True:
    print_board(chessboard)
    if player == 1:
        move = input("Player 1's turn: ")
    else:
        move = input("Player 2's turn: ")
    if move == "":
        quit()
    make_move(chessboard, move)
    player = 3 - player
