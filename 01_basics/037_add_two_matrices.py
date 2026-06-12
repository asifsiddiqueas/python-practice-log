import numpy as np

def add_matrices_numpy(A, B):
    # Convert standard Python lists to NumPy arrays
    np_A = np.array(A)
    np_B = np.array(B)
    
    # NumPy allows you to use the '+' operator directly on matrices
    return np_A + np_B

# --- 1. Define the matrices first ---
matrix_X = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

matrix_Y = [[9, 8, 7],
            [6, 5, 4],
            [3, 2, 1]]

# --- 2. Example Usage ---
print("NumPy Result:")
print(add_matrices_numpy(matrix_X, matrix_Y))
