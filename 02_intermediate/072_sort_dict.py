# Python program to sort Python Dictionaries by Key or Value.
def sort_dictionary(data_dict, by="key", descending=False):

    if by == "value":
        # sort by values instead of keys
        sorted_items = sorted(data_dict.items(), key=lambda item: item[1], reverse=descending)
    else:
        # default to sorting by keys
        sorted_items = sorted(data_dict.items(), reverse=descending)
        
    return dict(sorted_items)

# Example
scores = {
    'Charlie': 85,
    'Alice': 92,
    'Bob': 78,
    'Diana': 95
}

print(f"Original dictionary: {scores}\n")

# Sort by key (Alphabetical)
by_key = sort_dictionary(scores, by="key")
print(f"Sorted by Key:       {by_key}")

# Sort by value (Highest to Lowest)
by_value = sort_dictionary(scores, by="value", descending=True)
print(f"Sorted by Value:     {by_value}")