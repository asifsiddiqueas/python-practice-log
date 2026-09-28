"""
Python program to create a function that returns the binary (base-2) representation of a decimal (base-10) number.

Examples:
    binary(1) -> "1"
    binary(5) -> "101"
    binary(10) -> "1010"
"""

def binary(decimal_num: str | int) -> str:
    return bin(int(decimal_num))[2:]


if __name__ == "__main__":
    # Output from the function
    for val in (1, 5, 10):
        print(f"Binary representation of {val} is {binary(val)}")