#Skapa spelbrädan.
board = [[' ' for _ in range(3)] for _ in range(3)]

def draw_board():
    print(' ' + board[0][0] + ' | ' + board[0][1] + ' | ' + board[0][2] + ' ')
    print('-----------')
    print(' ' + board[1][0] + ' | ' + board[1][1] + ' | ' + board[1][2] + ' ')
    print('-----------')
    print(' ' + board[2][0] + ' | ' + board[2][1] + ' | ' + board[2][2] + ' ')
#Spelaren väljer vart dem vill kryssa.
def get_move(player):
    while True:
        move = input(f'{player}, enter your move (row column): ')
        try:
            row, col = map(int, move.split())
            if row in [0, 1, 2] and col in [0, 1, 2] and board[row][col] == ' ':
                board[row][col] = player
                break
            else:
                print('Invalid move, try again.')
        except ValueError:
            print('Invalid input, try again.')
def has_won(player):
    for row in board:
        if row == [player, player, player]:
            return True
    for col in range(3):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False-1
    
#Spelarna får resultat på själva matchen
def main():
    while True:
        draw_board()
        get_move('X')
        if has_won('X'):
            print('X has won!')
            break
        draw_board()
        get_move('O')
        if has_won('O'):
            print('O has won!')
            break

main()