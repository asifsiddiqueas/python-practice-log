"""
Computes the frequency of words from an input string and outputs them alphanumerically sorted by word.
Input: A string of whitespace-separated words (e.g., "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.")
Output: A newline-separated string of word frequencies formatted as 'word:count' (e.g., "2:2\n3.:1\n3?:1...")
"""

from collections import Counter

def calculate_word_frequencies(sentence):
    
    # tally word occurrences, sort alphabetically by key, and format the output
    counts = Counter(sentence.split())
    
    return '\n'.join(f"{word}:{count}" for word, count in sorted(counts.items()))

# test cases
input_data = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."

processed_data = calculate_word_frequencies(input_data)

print(f"Original text:\n{input_data}\n")
print(f"Frequencies:\n{processed_data}")
# expected output:
# 2:2
# 3.:1
# 3?:1
# New:1
# Python:5
# Read:1
# and:1
# between:1
# choosing:1
# or:2
# to:1