#!/usr/bin/python3
"""
The N queens puzzle is the challenge
of placing N non-attacking queens on an N×N chessboard
"""


import sys


class NQueensSolver:
    def __init__(self, n):
        """
        Initialize the NQueensSolver with the given board size.

        :param n: The size of the chessboard.
        """
        self.n = n
        self.column_for_row = [0] * (n + 1)
        self.solutions = []

    def is_safe_to_place_queen(self, row, col):
        """
        Check if it's safe to place a queen at a given position.

        :param row: The current row.
        :param col: The column to check.
        :return: True if it's safe to place a queen, False otherwise.
        """
        for prev_row in range(1, row):
            prev_col = self.column_for_row[prev_row]
            if prev_col == col or abs(prev_col - col) == abs(prev_row - row):
                return False
        return True

    def find_queen_placements(self, row):
        """
        Find all possible queen placements on the chessboard.

        :param row: The current row to consider.
        """
        for col in range(1, self.n + 1):
            if self.is_safe_to_place_queen(row, col):
                self.column_for_row[row] = col
                if row == self.n:
                    solution = [(r - 1, self.column_for_row[r] - 1)
                                for r in range(1, self.n + 1)]
                    self.solutions.append(solution)
                else:
                    self.find_queen_placements(row + 1)

    def solve_nqueens(self):
        """
        Find all solutions to the N-Queens problem
        and store them in self.solutions.
        """
        self.find_queen_placements(1)
        return self.solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    N = sys.argv[1]

    try:
        N = int(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solver = NQueensSolver(N)
    solutions = solver.solve_nqueens()

    for solution in solutions:
        formatted_solution = [[i, j] for i, j in solution]
        print(formatted_solution)
