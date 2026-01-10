"""
Project Euler Problem 004: https://projecteuler.net/problem=4

Largest Palindrome Product

A palindromic number reads the same both ways. The largest palindrome made from the product
of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

from helper_functions import is_prime


def is_palindrome(input: int | str) -> bool:
    """
    Determine whether the given input is a palindrome or not.

    >>> is_palindrome("melon")
    False
    >>> is_palindrome(9009)
    True
    >>> is_palindrome("tacocat")
    True
    >>> is_palindrome(123)
    False
    """
    str_input = str(input)
    return str_input == str_input[::-1]


def solution(digits: int = 3) -> int:
    """
    Returns the largest palindromic number using the product of numbers of a set digit length.

    >>> solution(2)
    9009
    """
    smallest_factor = int("1" + ("0" * (digits - 1)))
    largest_factor = int("9" * digits)
    min_number = smallest_factor * smallest_factor
    max_number = largest_factor * largest_factor

    for number in range(max_number, min_number, -1):
        if not is_palindrome(number) or is_prime(number):
            continue
        divisor = largest_factor
        while smallest_factor < divisor:
            factor = number // divisor
            # if our suspected palindrome is evenly divisible by our divisor and the product is within our target length, its a go
            if number % divisor == 0 and smallest_factor <= factor <= largest_factor:
                return number
            divisor -= 1

    raise Exception("No palindromes found.")


if __name__ == "__main__":
    print(f"{solution() = }")
