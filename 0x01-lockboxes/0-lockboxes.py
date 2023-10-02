#!/usr/bin/python3
"""
solving lockbox question
using Depth-First Search algorithm
"""


def canUnlockAll(boxes):
    """
    creating empty set to keep track of visited boxes
    """
    boxes_visited = set()

    """
    defining a Depth-First Search function algorithm
    It will help in exploring the boxes
    """
    def dfs(box):
        """
        marking the current boxes we have as visited
        by adding it to the set declared above
        """
        boxes_visited.add(box)
        """
        iterating through each key in the current boxes
        """
        for key in boxes[box]:
            if key not in boxes_visited:
                dfs(key)

    boxes_visited.add(0)
    """
    call dfs function and start exploring from box 0
    """
    dfs(0)

    """checking if all boxes were visited"""
    if len(boxes_visited) == len(boxes):
        return True
    return False
