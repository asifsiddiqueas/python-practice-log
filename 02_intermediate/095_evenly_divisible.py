"""
Python program to create a function that takes three arguments a, b, c and returns the sum of the
numbers that are evenly divided by c from the range a, b inclusive.

Examples:
    evenly_divisible(1, 10, 20) -> 0
    evenly_divisible(1, 10, 2) -> 30
    evenly_divisible(1, 10, 3) -> 18
"""

def evenly_divisible(a: int, b: int, c: int) -> int:
    return sum(num for num in range(a, b + 1) if num % c == 0)


if __name__ == "__main__":
    # Output from the function
    print(f"Sum of numbers between 1 and 10 divisible by 20 is {evenly_divisible(1, 10, 20)}")
    print(f"Sum of numbers between 1 and 10 divisible by 2 is {evenly_divisible(1, 10, 2)}")
    print(f"Sum of numbers between 1 and 10 divisible by 3 is {evenly_divisible(1, 10, 3)}")