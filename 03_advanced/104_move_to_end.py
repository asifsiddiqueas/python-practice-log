"""
Pyhton program to create a function that moves all elements of one type to the end of the list.

Examples:
    move_to_end([1, 3, 2, 4, 4, 1], 1) -> [3, 2, 4, 4, 1, 1]
    move_to_end([7, 8, 9, 1, 2, 3, 4], 9) -> [7, 8, 1, 2, 3, 4, 9]
    move_to_end(["a", "a", "a", "b"], "a") -> ["b", "a", "a", "a"]
"""

def move_to_end(lst: list, element) -> list:
    return [x for x in lst if x != element] + [x for x in lst if x == element]


if __name__ == "__main__":
    # Output from the function
    print(f"Result for [1, 3, 2, 4, 4, 1] with 1: {move_to_end([1, 3, 2, 4, 4, 1], 1)}")
    print(f"Result for [7, 8, 9, 1, 2, 3, 4] with 9: {move_to_end([7, 8, 9, 1, 2, 3, 4], 9)}")
    print(f"Result for ['a', 'a', 'a', 'b'] with 'a': {move_to_end(['a', 'a', 'a', 'b'], 'a')}")