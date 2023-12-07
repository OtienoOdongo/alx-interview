#!/usr/bin/python3
"""prime game"""


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
    if x < 1 or not nums:
        return None

    marias_wins, bens_wins = 0, 0
    max_n = max(nums)

    primes = [True for _ in range(1, max_n + 1, 1)]
    primes[0] = False

    for i, is_prime in enumerate(primes, 1):
        if i == 1 or not is_prime:
            continue
        for y in range(i + i, max_n + 1, i):
            primes[y - 1] = False

    for _, n in zip(range(x), nums):
        primes_count = len(list(filter(lambda x: x, primes[0: n])))
        bens_wins += primes_count % 2 == 0
        marias_wins += primes_count % 2 == 1

    if marias_wins == bens_wins:
        return None

    return 'Maria' if marias_wins > bens_wins else 'Ben'
