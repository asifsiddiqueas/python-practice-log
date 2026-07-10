# Python program to check if a given string is binary string or not.
def is_binary(text):
    # Safety check: an empty string isn't a valid binary string
    if not text:
        return False
        
    # Convert the string to a set of unique characters
    unique_chars = set(text)
    
    # Check if this set only contains '0' and/or '1'
    return unique_chars.issubset({'0', '1'})

# Testing
string1 = "10101001"
string2 = "10102001"

print(f"'{string1}' is binary: {is_binary(string1)}") # True
print(f"'{string2}' is binary: {is_binary(string2)}") # False