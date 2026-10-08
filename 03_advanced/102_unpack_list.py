"""
Python program to unpack the elements of a list into three variables: 'first', 'middle' (a list of all 
elements between the first and last), and 'last' using Python's extended unpacking syntax (*).

Examples:
    unpack([1, 2, 3, 4, 5, 6]) -> (1, [2, 3, 4, 5], 6)
    unpack(["a", "b", "c", "d"]) -> ("a", ["b", "c"], "d")
"""

def unpack(lst: list) -> tuple:
    first, *middle, last = lst
    return first, middle, last


if __name__ == "__main__":
    # Output from the function
    print(f"Result for [1, 2, 3, 4, 5, 6]: {unpack([1, 2, 3, 4, 5, 6])}")
    print(f"Result for ['a', 'b', 'c', 'd']: {unpack(['a', 'b', 'c', 'd'])}")