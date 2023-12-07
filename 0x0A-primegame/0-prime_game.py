#!/usr/bin/python3
"""prime game"""


def is_prime(num):
    """
    Check if a given number is prime.

    Parameters:
    - num (int): The number to check.

    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def get_primes_up_to_n(n):
    """
    Get a list of prime numbers up to a given number.

    Parameters:
    - n (int): The upper limit for prime numbers.

    Returns:
    list: A list of prime numbers up to n.
    """
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes


def isWinner(x, nums):
    """
    Determining the winner of a series of rounds in the prime number game.

    Parameters:
        x (int): The number of rounds.
        nums (list): An array of n for each round.

    Returns:
    str or None:
        The name of the player that won the most rounds.
        Returns None if the winner cannot be determined.
    """
    ben_wins = 0
    maria_wins = 0

    for n in nums:
        primes = get_primes_up_to_n(n)
        total_primes = len(primes)

        if total_primes % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if ben_wins > maria_wins:
        return "Ben"
    elif maria_wins > ben_wins:
        return "Maria"
    else:
        return None
