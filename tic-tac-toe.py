board = [["1","2","3"],
         ["4","5","6"],
         ["7","8","9"]]

player = "X"
def show_board(board):
    for row in board:
        print("|".join(row))


def winner(board, player):
    for i in range(3):
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True

    for i in range(3):
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return True

        if board[0][0] == player and board[2][2] == player and board[2][2] == player:
            return True
        if board[0][2] == player and board[2][2] == player and board[2][0] == player:
            return True

    return False


for plays in range(9):
    show_board(board)
    choice = input(f"Next Player: {player}, chose a posiction (1-9):")
    pos = int(choice) - 1
    line = pos // 3 
    row =  pos % 3

    if board[line][row] in ["X","O"]:
        print(f"chose another number")
        continue

    board[line][row] = player
    
    if winner(board, player):
        show_board(board)
        print(f"The Winner was: {player}")
        break

    if player == "O":
        player = "X"
    else:
        player = "O"

