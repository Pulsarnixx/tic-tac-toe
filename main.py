import random

"""Utilities for the tic-tac-toe-board"""
def display_board(board):
    '''
    The function prints board's current status.
    '''
    for row in board:
        print('+','+','+','+', sep='-------')
        print('|','|','|','|', sep='       ')
        print('|', row[0], '|', row[1], '|', row[2], '|', sep='   ')
        print('|','|','|','|', sep='       ')

    print('+','+','+','+', sep='-------')

def enter_move(board):
    '''
    The function accepts the board's current status, asks the user about their move, 
    checks the input, and updates the board according to the user's decision.
    '''
    try:
        move = int(input('Enter your move: '))
    except:
        print("Value type is not integer. Try again.")
        exit()

    if move not in make_list_of_free_fields(board):
        print("This field is not free! Try again.")
        exit()
    
    row = (move  - 1)// 3
    col = (move  - 1) % 3

    board[row][col] = 'O'

def make_list_of_free_fields(board):
    '''
    The function browses the board and builds a list of all the free squares.
    '''
    return [elem for row in board for elem in row if type(elem) is int]    

def victory_for(board, sign):
    '''
    The function analyzes the board's status in order to check if 
    the player using 'O's or 'X's has won the game
    '''
    pass

def draw_move(board):
    '''
    The function draws the computer's move and updates the board.
    '''

    free = make_list_of_free_fields(board)

    if len(free) == 9:
        board[1][1] = 'X'
    else:
        move = random.choice(free)
        
        row = (move  - 1)// 3
        col = (move  - 1) % 3

        board[row][col] = 'X'


    display_board(board)

board = [[3 * j + i + 1 for i in range(3)] for j in range(3)]

while len(make_list_of_free_fields(board)) > 1:

    draw_move(board)

    enter_move(board)

else:
    draw_move(board)

print("Program end.")