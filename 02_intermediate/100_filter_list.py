"""
Python program to create a function that takes a list of non-negative integers and strings 
and returns a new list without the strings.

Examples:
    filter_list([1, 2, "a", "b"]) -> [1, 2]
    filter_list([1, "a", "b", 0, 15]) -> [1, 0, 15]
    filter_list([1, 2, "aasf", "1", "123", 123]) -> [1, 2, 123]
"""

def filter_list(lst: list[int | str]) -> list[int]:
    return [item for item in lst if isinstance(item, int)]


if __name__ == "__main__":
    # Output from the function
    print(f"Result for [1, 2, 'a', 'b']: {filter_list([1, 2, 'a', 'b'])}")
    print(f"Result for [1, 'a', 'b', 0, 15]: {filter_list([1, 'a', 'b', 0, 15])}")
    print(f"Result for [1, 2, 'aasf', '1', '123', 123]: {filter_list([1, 2, 'aasf', '1', '123', 123])}")