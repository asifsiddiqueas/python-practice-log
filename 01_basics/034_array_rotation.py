def reverse_subarray(arr, start, end):
    """Helper function to reverse a portion of the array in-place."""
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def rotate_left_in_place(arr, d):
    n = len(arr)
    if n == 0:
        return
        
    d = d % n
    
    # 1. Reverse the first 'd' elements
    reverse_subarray(arr, 0, d - 1)
    
    # 2. Reverse the remaining elements
    reverse_subarray(arr, d, n - 1)
    
    # 3. Reverse the whole array
    reverse_subarray(arr, 0, n - 1)
    
    return arr

# --- Example Usage ---
my_array = [1, 2, 3, 4, 5, 6, 7]
print("\nOriginal:", my_array)
rotate_left_in_place(my_array, 2)
print("In-place left rotation by 2:", my_array)