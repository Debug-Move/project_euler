"""
Helpful functions written along the course of this project.
"""

import math
import typing as t


def is_prime(number: int) -> bool:
    """Checks to see if a number is prime, aka has two factors, 1 and itself.

    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(27)
    False
    >>> is_prime(2999)
    True
    >>> is_prime(0)
    False
    >>> is_prime(1)
    False
    """
    # if the number is equal or greater than 1, theres no effort required
    if number <= 1 or (number != 2 and number % 2 == 0):
        return False
    # we only need to look up to the numbers square root here.
    for i in range(2, int(math.sqrt(number))):
        if number % i == 0:
            return False

    return True  # if we get to this point, no factors exist


def prime_range(start: int, end: int) -> t.Generator[int, None, None]:
    """A generator that returns the next prime number in range"""
    for i in range(start, end, 1 if start < end else -1):
        if is_prime(i):
            yield i
