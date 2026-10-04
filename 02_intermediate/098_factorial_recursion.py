"""
Python program to create a function that calculates the factorial of a number recursively.

Examples:
    factorial(5) -> 120
    factorial(3) -> 6
    factorial(1) -> 1
    factorial(0) -> 1
"""

def factorial(n: int) -> int:
    if n <= 1:
        return 1
    return n * factorial(n - 1)


if __name__ == "__main__":
    # Output from the function
    for num in (5, 3, 1, 0):
        print(f"Factorial of {num} is {factorial(num)}")