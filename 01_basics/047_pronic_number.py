# Python program to print all pronic numbers between 1 and 100.
def is_pronic(n):
    """
    Checks if a given positive integer is a Pronic number.
    """
    # A clever math trick: the square root of a pronic number 
    # will always sit exactly between the two consecutive integers.
    # So, we find the integer square root of the number.
    root = int(n ** 0.5)
    
    # Check if multiplying that root by the next integer gives us our number
    return root * (root + 1) == n

print("Pronic numbers between 1 and 100 are:")

# Loop through numbers 1 to 100
for num in range(1, 101):
    if is_pronic(num):
        # Print on the same line, separated by a comma and space
        print(num, end=", ")

# A neat trick to clear the trailing comma and move to a new line at the end
print("\b\b ")