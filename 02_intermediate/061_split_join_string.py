# Python program to split and join a string.
def split_and_join(text):
    # 1. SPLIT: Break the string into a list of words
    # By default, .split() cuts the string at every space
    word_list = text.split()
    print(f"After splitting: {word_list}")
    
    # 2. JOIN: Glue the list back together into a single string
    # We put our desired glue (a hyphen) inside quotes, then call .join()
    joined_text = "-".join(word_list)
    print(f"After joining:   {joined_text}")
    
    return joined_text

# Example
my_string = "Python is an awesome programming language"
print(f"Original string: {my_string}\n")

# Run our function
result = split_and_join(my_string)