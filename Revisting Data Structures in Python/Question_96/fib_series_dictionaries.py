# -*- coding: utf-8 -*-
"""Untitled15.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1apvBYBoFA1BIel77UBxoAptEiJjF17cT
"""

def fib(n, memo={}):
    # Base case: fib(0) = 0, fib(1) = 1
    if n in (0, 1):
        return n

    # Check if the result for fib(n) is already memoized
    if n in memo:
        return memo[n]

    # Calculate fib(n) recursively
    result = fib(n - 1, memo) + fib(n - 2, memo)

    # Memoize the result for future use
    memo[n] = result

    return result

# Example usage
n = 10
result = fib(n)
print(f"The Fibonacci number at index {n} is: {result}")