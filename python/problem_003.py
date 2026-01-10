"""
Project Euler Problem 003: https://projecteuler.net/problem=3

Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""

from helper_functions import is_prime, prime_range

import math


def solution(number: int = 600851475143) -> int:
    """
    Returns the largest prime factor for the givin number.

    >>> solution(13195)
    29
    >>> solution(10)
    5
    >>> solution(17)
    17
    """
    # if the number is prime itself, then we already know its largest prime factor is itself
    if is_prime(number):
        return number
    primes = []
    quotient = 0
    for prime in prime_range(2, number):
        if (quotient and quotient % prime != 0) or number % prime != 0:
            # if we have a previous quotient it doesn't work with the current prime, we don't care.
            continue
        quotient = number // prime
        primes.append(prime)
        # if the product of all of our past primes equals our number, we have everything we need.
        if math.prod(primes) == number:
            return primes[-1]

    # fallback to what we have thus far
    return primes[-1] if primes else number


if __name__ == "__main__":
    print(f"{solution() = }")
