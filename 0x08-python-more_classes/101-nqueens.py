#!/usr/bin/python3
"""10. N queens"""

import sys


def create_new_board(n):
    """Function that creates new nxn sized chessboard with 0's."""

    board = []
    [board.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in board]
    return (board)


def copy_board(board):
    """Function that returns deepcopy of board"""

    if isinstance(board, list):
        return list(map(copy_board, board))

    return (board)


def find_method(board):
    """Function that finds solution for the Queen"""

    method = []
    for pos in range(len(board)):
        for position in range(len(board)):
            if board[pos][position] == "Q":
                method.append([pos, position])
                break

    return (method)


def invalid_moves(board, row, col):
    """Function that shows invalid moves for Queen"""

    for position in range(col + 1, len(board)):
        board[row][position] = "x"

    for position in range(col - 1, -1, -1):
        board[row][position] = "x"

    for pos in range(row + 1, len(board)):
        board[pos][col] = "x"

    for pos in range(row - 1, -1, -1):
        board[pos][col] = "x"

    c_pos = col + 1
    for pos in range(row + 1, len(board)):
        if c_pos >= len(board):
            break

        board[pos][c_pos] = "x"
        c_pos += 1

    c_pos = col - 1
    for pos in range(row - 1, -1, -1):
        if c_pos < 0:
            break

        board[pos][c_pos]
        c_pos -= 1

    c_pos = col + 1
    for pos in range(row - 1, -1, -1):
        if c_pos >= len(board):
            break

        board[pos][c_pos] = "x"
        c_pos += 1

    c_pos = col - 1
    for pos in range(row + 1, len(board)):
        if c_pos < 0:
            break

        board[pos][c_pos] = "x"
        c_pos -= 1


def correct_method(board, row, queens, solutions):
    """Function that solves puzzle with recursion"""

    if queens == len(board):
        solutions.append(find_method(board))
        return (solutions)

    for position in range(len(board)):
        if board[row][position] == " ":
            tmp_board = copy_board(board)
            tmp_board[row][position] = "Q"
            invalid_moves(tmp_board, row, position)
            solutions = correct_method(
                    tmp_board, row + 1, queens + 1, solutions)

    return (solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)

    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = create_new_board(int(sys.argv[1]))
    methods = correct_method(board, 0, 0, [])
    for sol in methods:
        print(sol)
