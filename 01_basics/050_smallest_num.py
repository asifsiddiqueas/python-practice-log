# Python program to find smallest number in a list.
def get_smallest_with_loop(numbers_list):
    """
    Finds the smallest number in a list by iterating through it.
    """
    # Safety check: if the list is empty, there is no smallest number!
    if not numbers_list:
        return None
        
    # Assume the first number is the smallest to start
    smallest = numbers_list[0]
    
    # Loop through the list to compare
    for number in numbers_list:
        # If we find a number smaller than our current 'smallest', update it
        if number < smallest:
            smallest = number
            
    return smallest

# Example Usage
my_numbers = [45, 12, 89, 3, 22]
result = get_smallest_with_loop(my_numbers)

print(f"The list: {my_numbers}")
print(f"The smallest number is: {result}")