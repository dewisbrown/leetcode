"""
36. Valid Sudoku

Determine if a 9 x 9 Sudoku board is valid. 
Only the filled cells need to be
validated according to the following rules:
    - Each row must contain the digits 1-9 without repetition.
    - Each column must contain the digits 1-9 without repetition.
    - Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
"""
from collections import defaultdict
def isValidSudoku(board: list[list[str]]) -> bool:
    """
    Uses dictionaries (hashmaps).
    """
    squares = defaultdict(set) # key = (r / 3, c / 3)
    rows = defaultdict(set)
    cols = defaultdict(set)

    for r in range(9):
        for c in range(9):
            if board[r][c] == '.':
                continue
            # check if character at coordinate exists in
            # the hashset at rows[r], cols[c], or
            # squares[(r // 3, c // 3)]
            if (board[r][c] in rows[r] or   # checks if char in hashset for row r
                board[r][c] in cols[c] or   # checks if char in hashset for col c
                board[r][c] in squares[(r // 3, c // 3)]):
                return False
            # if not, add it to the respective hashsets
            rows[r].add(board[r][c])
            cols[c].add(board[r][c])
            squares[(r // 3, c // 3)].add(board[r][c])
    return True
