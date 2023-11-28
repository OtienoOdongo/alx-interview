#!/usr/bin/python3
"""
a function that returns the perimeter
of the island described in grid
"""


from typing import List


def island_perimeter(grid: List[List[int]]) -> int:
    """
    Calculating the perimeter of the island in the grid.

    Args:
        grid (List[List[int]]):
        In the grid 0 represents water and 1 represents land.

    Returns:
        int: The perimeter of the island.
    """

    # Getting the number of rows and columns in the grid
    num_rows = len(grid)
    num_cols = len(grid[0])

    # Initializing counters for land cells and shared edges
    land_cells = 0
    shared_edges = 0

    # Iterating through each cell in the grid
    for i in range(num_rows):
        for j in range(num_cols):
            # Checking if the current cell contains land
            if grid[i][j] == 1:
                # Incrementing the count of land cells
                land_cells += 1

                # Checking the right neighbor
                if i + 1 < num_rows and grid[i + 1][j] == 1:
                    # If the right neighbor is land
                    # increment the shared edges count
                    shared_edges += 1

                # Checking the bottom neighbor
                if j + 1 < num_cols and grid[i][j + 1] == 1:
                    # If the bottom neighbor is land
                    # increment the shared edges count
                    shared_edges += 1

    # Calculating the final result based on the counts
    perimeter = land_cells * 4 - shared_edges * 2
    return perimeter
