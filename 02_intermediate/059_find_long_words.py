# Python program to find words which are greater than given length k.
def get_long_words(word_list, k):
    # Keep the word only if its length is strictly greater than k
    return [word for word in word_list if len(word) > k]

# Example
words = ["apple", "bat", "computer", "dog", "elephant", "car"]
min_length = 4

# Get the words longer than 4 characters
result = get_long_words(words, min_length)

# Print the result cleanly using an f-string
print(f"Words longer than {min_length} letters: {result}")