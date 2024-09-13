def display_title():
    print("Welcome to Tic Tac Toe")


def display_board(board):
    for row in range(3):
        print("+---+---+---+")
        print("|", board[row][0], "|", board[row][1], "|", board[row][2], "|")
    print("+---+---+---+")


def check_win(b, p):
    if b[0] == [p, p, p] or b[1] == [p, p, p] or b[2] == [p, p, p]:
        return True
    elif b[0][0]==p and b[1][1]==p and b[2][2]==p or b[0][2]==p and b[1][1]==p and b[2][0]==p:
        return True
        
    for col in range(len(b)):
        if b[0][col]== p and b[1][col]==p and b[2][col]==p:
            return True    


def main():
    board = [[' ', ' ', ' ' ], [' ', ' ', ' '], [' ', ' ', ' ']]
    display_title()
    display_board(board)
    player = "X"
    while True:
        print(f"Player {player} turn.")
        row = int(input("Pick a row (1, 2, 3): ")) - 1
        col = int(input("Pick a column (1, 2, 3): ")) - 1
        if 2 >= row >= 0 and 2>= col >= 0:
            if board[row][col] == ' ':
                board[row][col] = player
            else:
                print("invalid")  
                continue
            if check_win(board, player):
                display_board(board)
                break

            if player == 'X':
                player = 'O'
            else:
                player = 'X'
            display_board(board)
        else:
            print("Invalid input, try again\n")
    print(f"player {player} wins!")


if __name__ == "__main__":
    main()