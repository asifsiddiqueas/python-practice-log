# Python program for removing i th character from a string.
def remove_char_fast(text, index):
    # Safety check: if the index is out of bounds, just return the original text
    if index < 0 or index >= len(text):
        return text
        
    # Slice from the start up to the index, then add everything after the index
    return text[:index] + text[index+1:]

# Example
my_word = "GitHub"
remove_index = 3  # We want to remove the 'H' (index 3)

new_word = remove_char_fast(my_word, remove_index)

print(f"Original Word: {my_word}")
print(f"Cleaned Word:  {new_word}")