#!/usr/bin/python3
"""
calculating minimum number of operation
using prime factorization
"""


def minOperations(n):
    """
    Calculate the minimum number of operations
    required to achieve 'n' H characters.

    Args:
        n (int): The desired number of 'H' characters in the file.

    Returns:
        int: The minimum number of operations required
        to reach 'n' 'H' characters.
        If 'n' is impossible to achieve, it returns 0.
    """
    if n < 2:
        return 0

    min_operation = 0
    prime_factor = 2

    while prime_factor * prime_factor <= n:
        while n % prime_factor == 0:
            n //= prime_factor
            min_operation += prime_factor
        prime_factor += 1

    if n > 1:
        min_operation += n

    return min_operation
