#!/usr/bin/python3
"""
making changes algorithms
"""


def makeChange(coins, total):
    """
    Determining the fewest number of coins
    needed to meet a given amount total.

    Return:
        The fewest number of coins needed to meet the total.
        If total is 0 or less, return 0.
        If total cannot be met by any number of coins you have, return -1.
    """
    if total <= 0:
        return 0

    coins.sort()
    coins = coins[::-1]

    coins_used = 0
    remaining_amount = total

    for coin in coins:
        if coin <= remaining_amount:
            num_coins = remaining_amount // coin
            coins_used += num_coins
            remaining_amount -= num_coins * coin

    if remaining_amount == 0:
        return coins_used
    else:
        return -1
