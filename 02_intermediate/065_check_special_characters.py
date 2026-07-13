# Python Program to check if a string contains any special character.
import string

def contains_special_chars_simple(text):
    
    # Returns True if ANY character in the text is found in the punctuation list
    return any(char in string.punctuation for char in text)

# Example
string1 = "Hello World"
string2 = "Hello@World!"

print(f"'{string1}' has special characters: {contains_special_chars_simple(string1)}") # False
print(f"'{string2}' has special characters: {contains_special_chars_simple(string2)}") # True