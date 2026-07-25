"""
Calculates the total number of letters and digits in a given sentence.
Input: A string containing letters, digits, spaces, and symbols (e.g., "hello world! 123")
Output: A formatted string displaying the counts of letters and digits (e.g., "LETTERS 10\nDIGITS 3")
"""

def count_letters_and_digits(sentence):
    
    # use generators to sum boolean matches directly
    letters = sum(char.isalpha() for char in sentence)
    digits = sum(char.isdigit() for char in sentence)
    
    return f"LETTERS {letters}\nDIGITS {digits}"

# test cases
input_data = "hello world! 123"

processed_data = count_letters_and_digits(input_data)

print(f"Original sentence: {input_data}\n")
print(f"Processed output:\n{processed_data}")
# expected output: 
# LETTERS 10
# DIGITS 3