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

def get_best_row(board: dict, exclude: list):
    best_row, known = None, -1
    for row in range(1,10):
        if row in exclude: 
            continue
        count = 0
        for col in range(1,10):
            if board[row,col] is not None:
                count += 1
        if count > known and count < 9:
            known = count
            best_row = row
    return best_row

def examine_row(board, row):
    empty_cols = []
    needed = set(range(1,10))
    for col in range(1,10):
        if board[row,col] is None:
            empty_cols.append(col)
        if board[row,col] is not None:
            needed.remove(board[row,col])
    updated = False
    for col in empty_cols:
        possible = []
        for value in needed:
            c_check = check_column(board, col, value)
            b_check = check_box(board, row, col, value)
            if c_check and b_check:
                possible.append(value)
        if len(possible) == 1:
            board[row, col] = possible[0]
            updated = True

    return board, updated


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

def update_board(board):
    excluded = []
    updated = False
    while len(excluded) < 9:
        row = get_best_row(board, excluded)
        board, updated = examine_row(board, row)
        if updated:
            return board, updated
        excluded.append(row)
    else:
        print('Failed: no updates')
        return board, updated

def solved(board):
    for v in board.values():
        if v is None:
            return False
    return True
        
# ------------------------------------------------------------------------------

def main(board: dict):

    updated = True
    while not solved(board) and updated:
        board, updated = update_board(board)

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