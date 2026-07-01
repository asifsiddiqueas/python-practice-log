# Python program to print even numbers in a list.
def get_evens(nums):
    return [n for n in nums if n % 2 == 0]

# Our list of numbers
my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Get the evens
evens_only = get_evens(my_numbers)

# Printing the output...
print(f"The original numbers are: {my_numbers}")
print(f"The even numbers are: {evens_only}")