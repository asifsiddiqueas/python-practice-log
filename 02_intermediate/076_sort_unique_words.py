"""
Python program to Removes duplicate words from a whitespace-separated sequence and sorts them alphanumerically.
Input: A whitespace-separated string of words (e.g., "hello world and practice makes perfect and hello world again")
Output: A space-separated string of unique, sorted words (e.g., "again and hello makes perfect practice world")
"""
def sort_and_deduplicate(word_sequence):
    
    # dedupe using set, then sort and reconstruct the string
    return ' '.join(sorted(set(word_sequence.split())))

# test cases
input_data = "hello world and practice makes perfect and hello world again"

processed_data = sort_and_deduplicate(input_data)

print(f"Original sequence:  {input_data}")
print(f"Processed sequence: {processed_data}")
# expected output: again and hello makes perfect practice world