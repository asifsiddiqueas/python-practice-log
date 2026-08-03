"""
Python Program for a binary search function which Searches for a target item in a sorted list using the binary search algorithm.
Input: A sorted list of elements and a target item to search for.
Output: The integer index of the target item if found, otherwise -1.
"""

def binary_search(sorted_list, target):

    left, right = 0, len(sorted_list) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if sorted_list[mid] == target:
            return mid
        # adjust search window based on comparison
        elif sorted_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1

# test cases
data_list = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target_value = 23

index_found = binary_search(data_list, target_value)

print(f"Sorted list: {data_list}")
print(f"Target: {target_value}")
if index_found != -1:
    print(f"Element found at index: {index_found}")
else:
    print("Element not found in the list.")
# expected output: Element found at index: 5