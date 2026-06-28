# Python program to find largest number in a list.
"""
    This program is to inds the largest number in a list using Python's built-in max() function.
    """
def get_largest(numbers_list):

    # Pass the list into max() and it handles the rest
    return max(numbers_list)

# Example Usage...
my_numbers = [45, 12, 89, 3, 22]
result = get_largest(my_numbers)

print(f"The list: {my_numbers}")
print(f"The largest number is: {result}")