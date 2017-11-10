# sliding tiles puzzle
import random

def print_board(board):
    """ display the current board """

    board_size = len(board)
    
    print('The current board is')
    for i in range(board_size):
        for j in range(board_size):
            print(board[i][j],'',end='')
        print('')

def initialize_board(board):
    """ initialize the board """

    board_size = len(board)
    num_list = list(range(1,board_size*board_size))
    
    random.shuffle(num_list)
    num_list.append(0)
    
    index = 0
    for i in range(board_size):
        for j in range(board_size):
            board[i][j] = num_list[index]
            index += 1

def is_ended(board,sol_board):
    """ check if the game ends """
    
    is_end = True
    
    board_size = len(board)
    
    for i in range(board_size):
        for j in range(board_size):
            if board[i][j] != sol_board[i][j]:
                is_end = False
                break

    return is_end

def is_valid_move(board,move):
    """ check if the move is valid """
    
    is_valid = True
    board_size = len(board)
    
    # find the zero location
    row_index = 0
    col_index = 0
    
    for i in range(board_size):
        for j in range(board_size):
            if board[i][j] == 0:
                row_index = i
                col_index = j
                break
    
    if move != 'u' and move != 'd' and move != 'l' and move != 'r':
        is_valid = False
    elif row_index == 0 and move == 'd':
        is_valid = False
    elif row_index == board_size-1 and move == 'u':
        is_valid = False
    elif col_index == 0 and move == 'r':
        is_valid = False
    elif col_index == board_size-1 and move == 'l':
        is_valid = False
    
    return is_valid

def change_board(board,move):
    """ change the board according to the move """
    
    board_size = len(board)
    
    row_index = 0
    col_index = 0
    for i in range(board_size):
        for j in range(board_size):
            if board[i][j] == 0:
                row_index = i
                col_index = j
                break

    if move == 'u':
        board[row_index][col_index] = board[row_index+1][col_index]
        board[row_index+1][col_index] = 0
    elif move == 'd':
        board[row_index][col_index] = board[row_index-1][col_index]
        board[row_index-1][col_index] = 0
    elif move == 'l':
        board[row_index][col_index] = board[row_index][col_index+1]
        board[row_index][col_index+1] = 0
    elif move == 'r':
        board[row_index][col_index] = board[row_index][col_index-1]
        board[row_index][col_index-1] = 0
