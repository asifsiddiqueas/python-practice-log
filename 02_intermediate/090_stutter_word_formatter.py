"""
Python program that Formats a word to simulate a stuttering pronunciation by repeating its first two letters.
Input: A lowercase string 'word' containing at least two characters.
Output: A formatted string representing the stuttered word (Example: "in... in... incredible?").
"""

def stutter(word):
    
    # extract the first two characters and format
    first_two = word[:2]
    return f"{first_two}... {first_two}... {word}?"

# test cases
if __name__ == "__main__":
    print(stutter("incredible"))
    # expected output: in... in... incredible?
    
    print(stutter("enthusiastic"))
    # expected output: en... en... enthusiastic?
    
    print(stutter("outstanding"))
    # expected output: ou... ou... outstanding?