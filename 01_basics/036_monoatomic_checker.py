def is_monotonic_pythonic(arr):
    # An array with 1 or 0 elements is always monotonic
    if len(arr) <= 1:
        return True
    
    # Check if all elements are non-decreasing
    is_increasing = all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))
    
    # Check if all elements are non-increasing
    is_decreasing = all(arr[i] >= arr[i + 1] for i in range(len(arr) - 1))
    
    return is_increasing or is_decreasing

# --- Example Usage ---
print("Pythonic [1, 2, 2, 3]:", is_monotonic_pythonic([1, 2, 2, 3])) # True
print("Pythonic [6, 5, 4, 4]:", is_monotonic_pythonic([6, 5, 4, 4])) # True
print("Pythonic [1, 3, 2]:   ", is_monotonic_pythonic([1, 3, 2]))    # False
