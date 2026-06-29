# Python Program to finds the second largest number by removing duplicates and sorting.

def get_second_largest_simple(numbers_list):
    
    # Convert to a set to remove duplicate numbers, then back to a list
    unique_numbers = list(set(numbers_list))
    
    # Safety check...if we have less than 2 unique numbers, we can't find a second largest!
    if len(unique_numbers) < 2:
        return None
        
    # Sort the list in ascending order (smallest to largest)
    unique_numbers.sort()
    
    # Return the second-to-last item using negative indexing
    return unique_numbers[-2]

# Example
my_numbers = [10, 45, 89, 45, 89, 22]
result = get_second_largest_simple(my_numbers)

print(f"The list: {my_numbers}")
print(f"The second largest number is: {result}")