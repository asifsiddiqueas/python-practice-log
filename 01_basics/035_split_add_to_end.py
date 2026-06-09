def split_and_add_slicing(arr, k):
    """
    Splits the array at index k and moves the first part to the end.
    """
    n = len(arr)
    
    # Handle edge cases: empty array or k is 0
    if n == 0 or k <= 0:
        return arr
        
    # Safeguard in case k is larger than the array length
    k = k % n 
    
    # Slice from 'k' to the end, then concatenate from the start to 'k'
    return arr[k:] + arr[:k]

# --- Example Usage ---
my_array = [12, 10, 5, 6, 52, 36]
k_position = 2

print("Original array:  ", my_array)
print(f"Split at index {k_position}:", split_and_add_slicing(my_array, k_position))
