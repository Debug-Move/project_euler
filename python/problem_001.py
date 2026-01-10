"""
Project Euler Problem 001: https://projecteuler.net/problem=1

Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def solution(limit: int = 1000) -> int:
    """
    Returns the sum of all the multiples of 3 or 5 below n.

    >>> solution(10)
    23
    """
    answer = 0
    for i in range(limit):
        if i % 3 == 0 or i % 5 == 0:
            answer += i

    return answer


if __name__ == "__main__":
    print(f"{solution() = }")
