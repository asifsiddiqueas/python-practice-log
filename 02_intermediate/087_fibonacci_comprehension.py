"""
Computes and formats the Fibonacci Sequence up to n terms using recursion and a list comprehension.
Input: An integer n from the console representing the number of sequence terms to generate.
Output: A comma-separated string of the Fibonacci sequence (e.g., "0,1,1,2,3,5,8,13" for n=8)...
"""

from functools import lru_cache

# memoize previously computed numbers to avoid exponential recursive calls
@lru_cache(maxsize=None)
def fib(n):
    """Compute the nth Fibonacci number recursively."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n-1) + fib(n-2)

# test cases
if __name__ == "__main__":
    try:
        user_input = int(input("Enter an integer n: "))
        
        # calculate sequence up to n terms and format as a comma-separated string
        fib_sequence = [str(fib(i)) for i in range(user_input)]
        result = ",".join(fib_sequence)
        
        print(result)
        # expected output for n=7: 0,1,1,2,3,5,8
    except ValueError:
        print("Invalid input. Please enter an integer.")