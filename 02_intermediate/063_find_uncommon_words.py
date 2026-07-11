# program to find uncommon words from two Strings.
from collections import Counter

def get_uncommon_strict(str1, str2):
    # Combine both strings and split them into a single list of words
    all_words = str1.split() + str2.split()
    
    # Counter automatically counts how many times each word appears
    word_counts = Counter(all_words)
    
    # Return a list of words that appear exactly ONE time total
    return [word for word, count in word_counts.items() if count == 1]

# Example
sentence_1 = "apple banana apple"
sentence_2 = "banana orange grape"

print(f"Strict Uncommon Words: {get_uncommon_strict(sentence_1, sentence_2)}")
# Output: ['orange', 'grape']
# (Notice 'apple' is removed because it appeared twice in sentence 1)