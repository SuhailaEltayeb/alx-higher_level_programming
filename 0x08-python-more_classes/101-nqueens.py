#!/usr/bin/python3
"""Solves the N-queens puzzle.

Determines all possible solutions to placing N
non-attacking queens on an NxN chessboard.

Usage: nqueens N

N must be an integer greater than or equal to 4.

Each solution is represented as a list of queen positions:
[[r, c], [r, c], [r, c], [r, c]], where r and c represent
the row and column, respectively.

The program prints every possible solution to the problem, one
solution per line.
"""

import sys

def initialize_board(size):
    """Initialize an `size` x `size` chessboard with empty squares."""
    board = [[' '] * size for _ in range(size)]
    return board

def deepcopy_board(board):
    """Return a deepcopy of a chessboard."""
    if isinstance(board, list):
        return list(map(deepcopy_board, board))
    return board

def get_solution_positions(board):
    """Return the list of queen positions on a solved chessboard."""
    positions = []
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == "Q":
                positions.append([row, col])
                break
    return positions

def mark_attacked_spots(board, row, col):
    """Mark spots on the chessboard attacked by a queen."""
    size = len(board)
    
    for c in range(col + 1, size):
        board[row][c] = "x"  # Mark spots to the right
    
    for c in range(col - 1, -1, -1):
        board[row][c] = "x"  # Mark spots to the left
    
    for r in range(row + 1, size):
        board[r][col] = "x"  # Mark spots below
    
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"  # Mark spots above
    
    # Mark spots diagonally down to the right
    c = col + 1
    for r in range(row + 1, size):
        if c >= size:
            break
        board[r][c] = "x"
        c += 1
    
    # Mark spots diagonally up to the left
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1
    
    # Mark spots diagonally up to the right
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= size:
            break
        board[r][c] = "x"
        c += 1
    
    # Mark spots diagonally down to the left
    c = col - 1
    for r in range(row + 1, size):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1

def recursive_solve(board, row, queens, solutions):
    """Recursively solve an N-queens puzzle.

    Args:
        board (list): The current working chessboard.
        row (int): The current working row.
        queens (int): The current number of placed queens.
        solutions (list): A list of lists of solutions.

    Returns:
        solutions (list): A list of all solutions.
    """
    size = len(board)
    
    if queens == size:
        solutions.append(get_solution_positions(board))
        return solutions
    
    for col in range(size):
        if board[row][col] == " ":
            temp_board = deepcopy_board(board)
            temp_board[row][col] = "Q"
            mark_attacked_spots(temp_board, row, col)
            solutions = recursive_solve(temp_board, row + 1, queens + 1, solutions)

    return solutions

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    
    size = int(sys.argv[1])
    
    if size < 4:
        print("N must be at least 4")
        sys.exit(1)

    chessboard = initialize_board(size)
    solution_list = recursive_solve(chessboard, 0, 0, [])
    
    for solution in solution_list:
        print(solution)

