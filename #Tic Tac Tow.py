 #Fyra i rad
    

Player1=input("state your name player 1!")


Player2=input("and what would your name be player 2?")

position_p1=0#rename

position_p2=0


def printboard(board):
    for row in board:
        print(*row)

    print()

rows = 7
cols = 6
board =[["-" for _ in range(cols)]for _ in range(rows)]
print("1 2 3 4 5 6")
while True:
    printboard(board)
 

    Choice_row=input("which row do you want to cross off player 1?").lower()
    print("")

    board[1][1] = "X"

    printboard(board)


    Choice_row=input(f"which row do you want to cross off {Player1}?").lower()
    print("")
    
    board[1][1] = "X"

    printboard(board)

    Choice_row=input(f"which row do you want to cross off {Player2}?").lower()
    print("") 

    board[1][1] = "X"
rows=6
