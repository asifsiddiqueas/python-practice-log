#  Python program to find the N largest numbers by sorting the list and slicing it.
def get_n_largest_simple(numbers_list, n):
    # Sort the list from highest to lowest (reverse=True)
    # Then use list slicing [:n] to grab exactly the first 'n' elements
    return sorted(numbers_list, reverse=True)[:n]

# Example
my_numbers = [45, 12, 89, 3, 22, 105, 76]
top_count = 3

result = get_n_largest_simple(my_numbers, top_count)

print(f"The list: {my_numbers}")
print(f"The top {top_count} largest numbers are: {result}")