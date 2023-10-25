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
    A function that validates UTF-8 encoding.

    Args:
    data (List[int]): List of integers representing the UTF-8 data.

    Returns:
    bool: True if the data is a valid UTF-8 encoding, False otherwise.
    """
    valid_byte = 0
    for byte in data:
        if valid_byte == 0:
            """starting with 1 byte character validation"""
            if (byte >> 7) == 0b0:
                valid_byte = 0
            """Then 2 byte character validation"""
            elif (byte >> 5) == 0b110:
                valid_byte = 1
            """Then 3 byte caharacter valaidation"""
            elif (byte >> 4) == 0b1110:
                valid_byte = 2
            """Then 4 byte character validation"""
            elif (byte >> 3) == 0b11110:
                valid_byte = 3
            else:
                return False
        else:
            """Ending with a byte that starts with 10"""
            if (byte >> 6) != 0b10:
                return False
            valid_byte -= 1

    return valid_byte == 0
