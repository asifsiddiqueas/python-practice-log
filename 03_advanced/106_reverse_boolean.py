"""
Python program to create a function that reverses a boolean value and returns the string 
"boolean expected" if another variable type is given.

Examples:
    reverse(True) -> False
    reverse(False) -> True
    reverse(0) -> "boolean expected"
    reverse(None) -> "boolean expected"
"""

def reverse(arg):
    if type(arg) is not bool:
        return "boolean expected"
    return not arg


if __name__ == "__main__":
    # Output
    print(f"Result for True: {reverse(True)}")
    print(f"Result for False: {reverse(False)}")
    print(f"Result for 0: {reverse(0)}")
    print(f"Result for None: {reverse(None)}")