"""Accepts a comma-separated sequence of words and returns them sorted alphabetically.
Input: A comma-separated string of words (e.g., "without,hello,bag,world")
Output: A comma-separated string of sorted words (e.g., "bag,hello,without,world")"""

def sort_words_alphabetically(word_sequence):

    # 1. split(',') breaks the string into a list of words
    # 2. sorted() arranges that list alphabetically
    # 3. ','.join() stitches the sorted list back into a single string
    return ','.join(sorted(word_sequence.split(',')))

# Example
input_data = "without,hello,bag,world"

processed_data = sort_words_alphabetically(input_data)

print(f"Original sequence:  {input_data}")
print(f"Processed sequence: {processed_data}")
# Output: Processed sequence: bag,hello,without,world