# python program to find sum of element in list.
def sum_with_loop(numbers_list):
    """
    Finds the sum of a list by iterating through each element.
    """
    # Start our running total at 0
    total = 0
    
    # Loop through every number in the list
    for number in numbers_list:
        # Add the current number to our total
        total += number
        
    return total

# --- Example Usage ---
my_numbers = [10, 20, 30, 40, 50]
result = sum_with_loop(my_numbers)

print(f"The list: {my_numbers}")
print(f"The total sum is: {result}")