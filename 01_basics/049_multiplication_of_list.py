# Python program to Multiply all numbers in the list.
def multiply_with_loop(numbers_list):
    """
    Multiplies all numbers in a list by iterating through each element.
    """
    # Start our running total at 1 (not 0!)
    total = 1
    
    # Loop through every number in the list
    for number in numbers_list:
        # Multiply the current number by our total
        total *= number
        
    return total

# Example Usage
my_numbers = [2, 3, 4, 5]
result = multiply_with_loop(my_numbers)

print(f"The list: {my_numbers}")
print(f"The total product is: {result}")