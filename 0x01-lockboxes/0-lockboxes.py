#!/usr/bin/python3
"""
solving lockbox question
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
    boxes (list of lists):
    A list of lists representing the boxes and their key contents.

    Returns:
    bool: True if all boxes can be opened, False otherwise.
    """

    """
    Create a list to keep track of keys we have
    initially with the first key (box 0)
    """
    keys = [0]

    """
    Iterate through the keys list and simulate the process of unlocking boxes
    """
    for key in keys:
        """Get the contents of the current box"""
        box_contents = boxes[key]

        """Iterate through the keys found in the current box's contents"""
        for new_key in box_contents:
            """
            Check if the new key is not already in our possession
            and it corresponds to a valid box
            """
            if new_key not in keys and 0 <= new_key < len(boxes):
                keys.append(new_key)

    """Check if we have collected keys for all boxes"""
    if len(keys) == len(boxes):
        return True
    else:
        return False
