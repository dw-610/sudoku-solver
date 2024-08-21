"""
This script solves a sudoku puzzle.
"""

# ------------------------------------------------------------------------------
# functions

def print_board(board: dict):
    print('-------------------------')
    for i in range(1,10):
        for j in range(1,10):
            value = '_' if board[i,j] is None else board[i,j]
            value = '_' if isinstance(value, set) else value
            if j == 1:
                print(f'| {value}', end=' ')
            elif j % 3 == 0:
                print(f'{value} |', end='')
            elif j % 3 == 1:
                print(f' {value}', end=' ')
            else:
                print(value, end=' ')
        if i % 3 == 0:
            print('\n-------------------------')
        else:
            print()

def check_column(board: dict, col: int, value: int):
    for row in range(1,10):
        if board[row,col] is not None and board[row,col] == value:
            return False
    return True

def check_box(board: dict, row: int, col: int, value: int):
    if row <= 3:
        if col <= 3:
            for i in range(1,4):
                for j in range(1,4):
                    if board[i,j] is not None and board[i,j] == value:
                        return False
        elif col <= 6:
            for i in range(1,4):
                for j in range(4,7):
                    if board[i,j] is not None and board[i,j] == value:
                        return False
        else:
            for i in range(1,4):
                for j in range(7,10):
                    if board[i,j] is not None and board[i,j] == value:
                        return False
    elif row <= 6:
        if col <= 3:
            for i in range(4,7):
                for j in range(1,4):
                    if board[i,j] is not None and board[i,j] == value:
                        return False
        elif col <= 6:
            for i in range(4,7):
                for j in range(4,7):
                    if board[i,j] is not None and board[i,j] == value:
                        return False
        else:
            for i in range(4,7):
                for j in range(7,10):
                    if board[i,j] is not None and board[i,j] == value:
                        return False
    else:
        if col <= 3:
            for i in range(7,10):
                for j in range(1,4):
                    if board[i,j] is not None and board[i,j] == value:
                        return False
        elif col <= 6:
            for i in range(7,10):
                for j in range(4,7):
                    if board[i,j] is not None and board[i,j] == value:
                        return False
        else:
            for i in range(7,10):
                for j in range(7,10):
                    if board[i,j] is not None and board[i,j] == value:
                        return False
    return True

def prune_row(board: dict, row: int, value: int):
    for col in range(1,10):
        if isinstance(board[row,col], set) and value in board[row,col]:
            board[row,col].remove(value)

def prune_column(board: dict, col: int, value: int):
    for row in range(1,10):
        if isinstance(board[row,col], set) and value in board[row,col]:
            board[row,col].remove(value)

def prune_box(board: dict, row: int, col: int, value: int):
    if row <= 3:
        if col <= 3:
            for i in range(1,4):
                for j in range(1,4):
                    if isinstance(board[i,j], set) and value in board[i,j]:
                        board[i,j].remove(value)
        elif col <= 6:
            for i in range(1,4):
                for j in range(4,7):
                    if isinstance(board[i,j], set) and value in board[i,j]:
                        board[i,j].remove(value)
        else:
            for i in range(1,4):
                for j in range(7,10):
                    if isinstance(board[i,j], set) and value in board[i,j]:
                        board[i,j].remove(value)
    elif row <= 6:
        if col <= 3:
            for i in range(4,7):
                for j in range(1,4):
                    if isinstance(board[i,j], set) and value in board[i,j]:
                        board[i,j].remove(value)
        elif col <= 6:
            for i in range(4,7):
                for j in range(4,7):
                    if isinstance(board[i,j], set) and value in board[i,j]:
                        board[i,j].remove(value)
        else:
            for i in range(4,7):
                for j in range(7,10):
                    if isinstance(board[i,j], set) and value in board[i,j]:
                        board[i,j].remove(value)
    else:
        if col <= 3:
            for i in range(7,10):
                for j in range(1,4):
                    if isinstance(board[i,j], set) and value in board[i,j]:
                        board[i,j].remove(value)
        elif col <= 6:
            for i in range(7,10):
                for j in range(4,7):
                    if isinstance(board[i,j], set) and value in board[i,j]:
                        board[i,j].remove(value)
        else:
            for i in range(7,10):
                for j in range(7,10):
                    if isinstance(board[i,j], set) and value in board[i,j]:
                        board[i,j].remove(value)
    return board

def solved(board):
    if any([isinstance(v,set) for v in board.values()]):
        return False
    else:
        return True

def simple_step(board: dict, blank: set):
    updated = False
    for row, col in blank:
        if len(board[row,col]) == 1:
            board[row,col] = board[row,col].pop()
            u_row, u_col, u_val = row, col, board[row,col]
            updated = True
            break
    if updated:
        return board, updated, u_row, u_col, u_val
    else:
        return board, updated, None, None, None
    
def prepare_board(board: dict):
    blank = set()
    for row in range(1,10):
        empty_cols = set()
        needed = set(range(1,10))
        for col in range(1,10):
            if board[row,col] is None:
                empty_cols.add(col)
                blank.add((row,col))
            if board[row,col] is not None:
                needed.remove(board[row,col])
        for col in empty_cols:
            possible = set()
            for value in needed:
                c_check = check_column(board, col, value)
                b_check = check_box(board, row, col, value)
                if c_check and b_check:
                    possible.add(value)
            board[row,col] = possible
    return board, blank

# ------------------------------------------------------------------------------

def main(board: dict):
    board, blank = prepare_board(board)    
    while not solved(board):
        board, updated, u_row, u_col, u_val = simple_step(board, blank)
        if updated:
            blank.remove((u_row, u_col))
            prune_row(board, u_row, u_val)
            prune_column(board, u_col, u_val)
            prune_box(board, u_row, u_col, u_val)
        else:
            print('\nNo one-step updates found!')
            return board
    return board

# ------------------------------------------------------------------------------

if __name__ == '__main__':

    unsolved = {}
    for i in range(1,10):
        for j in range(1,10):
            unsolved[i,j] = None

    given = {
        (1,2): 8, (1,3): 6, (1,6): 5, 
        (2,2): 9, (2,7): 6, (2,9): 8,
        (3,1): 3, (3,3): 2, (3,5): 8, (3,7): 5,
        (4,2): 6, (4,3): 4, (4,5): 2, (4,6): 8,
        (5,4): 3, (5,6): 9, 
        (6,4): 4, (6,5): 7, (6,7): 1, (6,8): 8,
        (7,3): 3, (7,5): 6, (7,7): 4, (7,9): 5,
        (8,1): 9, (8,3): 7, (8,8): 3,
        (9,4): 5, (9,7): 8, (9,8): 7
    }

    for k, v in given.items():
        unsolved[k] = v

    print('\nPuzzle:')
    print_board(unsolved)

    solved = main(unsolved)

    print('\nSolved:')
    print_board(solved)

# ------------------------------------------------------------------------------