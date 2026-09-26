"""
Python program to Check if a non-negative integer 'num' is a Curzon number.
A number is a Curzon number if (2^num + 1) is exactly divisible by (2*num + 1).

Examples:
    is_curzon(5) -> True
    is_curzon(10) -> False
    is_curzon(14) -> True
"""

def is_curzon(num: int) -> bool:
    power_term = (2 ** num) + 1
    mult_term = (2 * num) + 1
    
    return power_term % mult_term == 0


if __name__ == "__main__":
    # Output from the function
    for n in (5, 10, 14):
        print(f"Is {n} a Curzon number? {is_curzon(n)}")