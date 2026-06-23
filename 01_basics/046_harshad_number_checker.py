# python program to determine whether the given number is a Harshad Number.

# A Harshad Number (sometimes called a Niven number) is an integer that is perfectly divisible by the sum of its digits.

# For example, 18 is a Harshad number because...
# The sum of its digits is 1 + 8 = 9
# 18 is perfectly divisible by 9 (18 / 9 = 2 with a remainder of 0)

def is_harshad_number(n):
    """
    Checks if a given positive integer is a Harshad Number.
    """
    # Harshad numbers are strictly positive integers
    if n <= 0:
        return False
        
    # Convert the number to a string to easily loop through each digit,
    # convert them back to integers, and sum them up.
    digit_sum = sum(int(digit) for digit in str(n))
    
    # Check if the original number modulo the digit sum is 0
    # (Meaning it divides perfectly with no remainder)
    return n % digit_sum == 0

# Test it out
# You can change this value to test other numbers (e.g., 21, 153, 19)
test_number = 18 

if is_harshad_number(test_number):
    print(f"{test_number} is a Harshad Number!")
else:
    print(f"{test_number} is NOT a Harshad Number.")