# Python program to find all duplicate characters in string using Python's built-in Counter.
from collections import Counter

def find_duplicates_fast(text):
    # Counter creates a dictionary of {character: count}
    char_counts = Counter(text)
    
    # Use a list comprehension to keep only characters that appear more than once
    return [char for char, count in char_counts.items() if count > 1]

# Example
my_string = "programming"
duplicates = find_duplicates_fast(my_string)

print(f"Original string: '{my_string}'")
print(f"Duplicate characters: {duplicates}")
# Output: ['r', 'g', 'm']