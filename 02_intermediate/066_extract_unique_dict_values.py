# Python program to Extract Unique dictionary values.
def get_unique_values_fast(data_dict):

    # 1. data_dict.values() grabs all the values (ignoring the keys)
    # 2. set() automatically removes any duplicates
    # 3. list() converts it back into a standard Python list
    return list(set(data_dict.values()))

# Example
my_dict = {
    'apple': 10,
    'banana': 20,
    'cherry': 10,  # Duplicate value!
    'date': 30,
    'elderberry': 20 # Duplicate value!
}

unique_vals = get_unique_values_fast(my_dict)

print(f"Original dictionary: {my_dict}")
print(f"Unique values: {unique_vals}")
# Output: [10, 20, 30] (Order may vary since sets do not track order)