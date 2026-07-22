"""Generates an X by Y 2-dimensional array where the value at (i, j) is i * j.
Input: A comma-separated string representing dimensions X,Y (e.g., "3,5")
Output: A nested list representing the 2D array (e.g., [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]])"""

def generate_2d_array(dimensions):

    # parse dimensions from comma-separated string
    x, y = map(int, dimensions.split(','))
    
    # build grid using a nested list comprehension
    return [[i * j for j in range(y)] for i in range(x)]

# Example Usage
input_data = "3,5"

processed_data = generate_2d_array(input_data)

print(f"Original dimensions: {input_data}")
print(f"Processed array:     {processed_data}")
# expected output: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]