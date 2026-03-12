#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
    ---------------------
    Recursively computes the factorial of a non-negative integer n.

    Parameters:
    ------------
    n : int
        A non-negative integer whose factorial is to be computed.

    Returns:
    ---------
    int
        The factorial of the given number n.
    """
    if n == 0:
        return 1  # Base case: factorial of 0 is 1
    else:
        return n * factorial(n-1)  # Recursive case: n! = n * (n-1)!

# Get the input number from the command line argument
f = factorial(int(sys.argv[1]))

# Print the result
print(f)
