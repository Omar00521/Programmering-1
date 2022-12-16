#fyra i rad
import random
from secrets import choice

choice_cols=[]
choice_row=[]

def won(board):
    for row in board:
        if all(x == "X" for x in row):
            return True
        if all(x == "Y" for x in row):
            return True
    for i in range(len(board)):
        if all(board[j][i] == "X" for j in range(len(board))):
            return True
        if all(board[j][i] == "O" for j in range(len(board))):
            return True


#Spelarna väljer sina namn.
Player1=input("state your name player 1!")


Player2=input("and what would your name be player 2?")

position_p1=0#rename

position_p2=0

#Detta printar fram spelplanen.
def printboard(board):
    for row in board:
        print(*row)
    print("1 2 3 4 5 6 7 ")

#Rader och kolumner
rows=6
cols=7

#Spelarna kan då völja vart dem vill placera sina märken inom raderna samt kolumnern.
board =[["-" for _ in range(cols)]for _ in range(rows)]
printboard(board)
play_again= True
while play_again:
    print(f"Your turn {Player1}")
    choice_row=int(input(f"which row do you want to cross off {Player1}?")) -1
    choice_row=int(input(f"which column do you want to cross off {Player1}?")) -1

    #spelarna tyras om med att markea vart dem vill sätta sina märken för att kunna få fyra i rad.
    board[choice_row][choice_cols] = "X"
    won(board)
    printboard(board)

    print(f"Your turn {Player2}")
    choice_row=int(input(f"which row do you want to cross off {Player2}?")) -1
    choice_row=int(input(f"which column do you want to cross off {Player2}?")) -1

    board[choice_row][choice_cols] = "O"
    won(board)
    printboard(board)   
