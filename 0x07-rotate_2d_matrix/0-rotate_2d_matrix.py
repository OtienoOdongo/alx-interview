#!/usr/bin/python3
"""
Rotating a 2D matrix 90 degrees clockwise
"""


def rotate_2d_matrix(matrix):
    """
    Rotating a 2D matrix 90 degrees clockwise

    Args:
    Matrix: The input 2D matrix to be rotated.

    Returns:
    None: The matrix is rotated in-place.
    """
    matrix[:] = [list(row) for row in zip(*reversed(matrix))]
