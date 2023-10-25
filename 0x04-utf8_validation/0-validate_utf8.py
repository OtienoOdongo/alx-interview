#!/usr/bin/python3
"""
UTF-8 Validation exercise
In utf-8 validation the following is checked:
if the binary value starts with 0 it takes 1 byte
if the binary value starts with 110 it takes 2 byte
if the binary value starts with 1110 it takes 3 byte
if the binary value starts with 11110 it takes 4 byte
if the binary value starts with 10
it takes 2nd,3rd,or 4th of
110, 1110, or 11110 binary value
"""


from typing import List


def validUTF8(data: List[int]) -> bool:
    """
    Validate whether a given list of integers
    represents a valid UTF-8 encoding.

    Args:
        data (List[int]): List of integers representing the UTF-8 data.

    Returns:
        bool: True if the data is a valid UTF-8 encoding, False otherwise.
    """

    # Initializing the variable to keep track
    # of the expected number of continuation bytes
    valid_byte = 0

    for byte in data:
        if valid_byte == 0:
            # Checking if the byte indicated starts with a 4byte character
            if (byte >> 3) == 0b11110:
                valid_byte = 3
            # Checking if the byte indicated starts with a 3byte character
            elif (byte >> 4) == 0b1110:
                valid_byte = 2
            # Checking if the byte indicated the starts with a 2byte character
            elif (byte >> 5) == 0b110:
                valid_byte = 1
            # Checking if the byte indicated starts with a 1-byte character
            elif (byte >> 7) == 0b0:
                valid_byte = 0
            else:
                # Invalid starting byte for a character
                return False
        else:
            # Ensure continuation bytes start with '10'
            if (byte >> 6) != 0b10:
                # Invalid continuation byte
                return False
            valid_byte -= 1

    # If valid_byte is zero at the end
    # all characters were properly terminated
    return valid_byte == 0
