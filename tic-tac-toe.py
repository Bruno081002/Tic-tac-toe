board = [["1","2","3"],
         ["4","5","6"],
         ["7","8","9"]]

player = "X"
def show_board(board):
    for row in board:
        print("|".join(row))

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

    if player == "O":
        player = "X"
    else:
        player = "O"

