# Python program to check order of character in string using OrderedDict().
from collections import OrderedDict

def check_character_order(text, pattern):

    # deduplicate text chars while preserving original order
    unique_chars_dict = OrderedDict.fromkeys(text)
    
    pattern_index = 0
    
    for char in unique_chars_dict:
        # advance pattern pointer on match
        if char == pattern[pattern_index]:
            pattern_index += 1
            
        # stop early if the entire pattern is matched
        if pattern_index == len(pattern):
            return True
            
    return False

# test cases
my_string = "engineers rock"
my_pattern = "egr"
bad_pattern = "rge"

print(f"Original string: '{my_string}'")

is_ordered_1 = check_character_order(my_string, my_pattern)
print(f"Pattern '{my_pattern}' in order? {is_ordered_1}") # expected: True

is_ordered_2 = check_character_order(my_string, bad_pattern)
print(f"Pattern '{bad_pattern}' in order? {is_ordered_2}") # expected: False