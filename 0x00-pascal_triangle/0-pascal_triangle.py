#!/usr/bin/python3

def pascal_triangle(n):
    # Check if n is less than or equal to 0, return an empty list
    if n <= 0:
        return []
    
    # Initialize a list to store Pascal's triangle
    pascal_t = []
    
    # Loop through each row of Pascal's triangle
    for i in range(n):
        # Initialize an empty list for the current row
        row = []
        
        # Loop through each position in the current row
        for j in range(i + 1):
            # If j is the first or last element in the row, it's always 1
            if j == 0 or j == i:
                row.append(1)
            else:
                # Calculate the value based on the values in the previous row
                row.append(pascal_t[i - 1][j - 1] + pascal_t[i - 1][j])
        
        # Append the current row to Pascal's triangle
        pascal_t.append(row)
    
    # Return the Pascal's triangle as a list of lists
    return pascal_t
