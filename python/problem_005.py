"""
Project Euler Problem 005: https://projecteuler.net/problem=5

Smallest multiple

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is _evenly divisible_ by all
of the numbers from 1 to 20?
"""

import math
import typing as t
from functools import reduce


def least_common_multiplier(*args: t.Sequence[int]) -> int:
    """
    Find the smallest positive integer divisible by two or more given numbers.

    >>> least_common_multiplier(7, 2, 3, 5, 4)
    420
    """

    def _least_common_multiplier(a: int, b: int) -> int:
        if a == 0 or b == 0:
            return 0
        return abs(a * b) // math.gcd(a, b)

    if 0 in args or len(args) < 2:
        return 0
    return reduce(_least_common_multiplier, args)


def solution_1(range_min: int = 1, range_max: int = 20) -> int:
    """
    Returns the smallest positive number evenly divisible by all numbers in range.

    >>> solution(1, 10)
    2520
    >>> solution(1, 20)
    232792560
    """
    out_number = 1
    solution_found = False
    while not solution_found:
        for i in range(range_min, range_max + 1):
            if out_number % i != 0:
                break
        if i == range_max and out_number % i == 0:
            solution_found = True
        else:
            out_number += 1
    return out_number


def solution_2(range_min: int = 1, range_max: int = 20) -> int:
    """
    Returns the smallest positive number evenly divisible by all numbers in range.

    >>> solution(1, 10)
    2520
    >>> solution(1, 20)
    232792560
    """
    return least_common_multiplier(*range(range_min, range_max + 1))


def solution_3(range_min: int = 1, range_max: int = 20) -> int:
    """
    Alternatively, this is much faster but but more obscured as only a true mathematician would know whats going on.
    Thanks to Python 3.9+ for adding such complicated math.
    """
    return math.lcm(*range(range_min, range_max + 1))


if __name__ == "__main__":
    # clear winner in terms of speed
    print(f"{solution_3() = }")
