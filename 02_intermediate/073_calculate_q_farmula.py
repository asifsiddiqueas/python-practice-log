"""Python Progran to calculates the formula: Q = Square root of (2 * C * D) / H
Fixed values: C = 50, H = 30
Input should be: A comma-separated string of variable 'D' values (e.g., "100,150,180")
Output should be: A comma-separated string of evaluated 'Q' values (e.g., "18,22,24")"""
import math

def calculate_formula(d_sequence):
    C = 50
    H = 30
    
    # apply formula to each parsed int and cast results back to string for joining
    results = [
        str(int(math.sqrt((2 * C * int(d)) / H))) 
        for d in d_sequence.split(',')
    ]
    
    return ','.join(results)

# test execution
input_data = "100,150,180"

processed_data = calculate_formula(input_data)

print(f"Original sequence:  {input_data}")
print(f"Processed sequence: {processed_data}")
# expected output: 18,22,24