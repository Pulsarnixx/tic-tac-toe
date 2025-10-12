import random

"""Utilities for the tic-tac-toe-board"""
def display_board(board: list[list]) -> None:
    '''
    The function prints board's current status.
    '''
    for row in board:
        print('+','+','+','+', sep='-------')
        print('|','|','|','|', sep='       ')
        print('|', row[0], '|', row[1], '|', row[2], '|', sep='   ')
        print('|','|','|','|', sep='       ')

    print('+','+','+','+', sep='-------')

def enter_move(board: list[list]) -> None:
    '''
    The function accepts the board's current status, asks the user about their move, 
    checks the input, and updates the board according to the user's decision.
    '''
    free: list[int] = make_list_of_free_fields(board)

    while True:
        try:
            move: int = int(input('Enter your move (1-9): '))
        except:
            print("Value type is not int. Try again.")
            continue

        if move not in free:
            print("This field is not free or out of range! Try again.")
            continue

        row, col = (move  - 1)// 3, (move  - 1) % 3
        board[row][col] = 'O'

        return

def make_list_of_free_fields(board: list[list]) -> list[int]:
    '''
    The function browses the board and builds a list of all the free squares.
    '''
    return [elem for row in board for elem in row if type(elem) is int]    

def victory_for(board: list[list], sign: str = 'X') -> bool:
    '''
    The function analyzes the board's status in order to check if 
    the player using 'O's or 'X's has won the game
    '''
    if sign != 'O' and sign != 'X':
        return False

    #Vertical & Horizontal

    for i in range(3):
        #Rows
        if all([board[i][j] == sign for j in range(3)]):
            return True
        
        #Cols
        if all([board[j][i] == sign for j in range(3)]):
            return True
    
    #Diagonal
    if all([board[i][i] == sign for i in range(3)]):
            return True
    
    if all([board[i][2-i] == sign for i in range(3)]):
            return True

    return False

def draw_move(board: list[list]) -> None:
    '''
    The function draws the computer's move and updates the board.
    '''

    free: list[int] = make_list_of_free_fields(board)

    if len(free) == 9:
        board[1][1] = 'X'
    else:
        move = random.choice(free)
        
        row, col = (move  - 1)// 3, (move  - 1) % 3
        board[row][col] = 'X'

    display_board(board)

board: list[list[int]] = [[3 * j + i + 1 for i in range(3)] for j in range(3)]

winner: str | None = None

print("Welcome to Tic-Tac-Toe!")
print("You play as O. Computer plays as X.")

for i in range(4):
    draw_move(board)

    if victory_for(board):
        winner = 'Bot'
        break;

    enter_move(board)

    if victory_for(board, 'O'):
        display_board(board)
        winner = 'Player'
        break;

print("Draw") if winner is None else print("Winner:", winner)