import numpy as np

# Defining the function
def multiply_numpy_array(A, B):
    np_A = np.array(A)
    np_B = np.array(B)

# return of this defined function
    return np_A * np_B

# Predefined matrices as mat..X and mat...Y
matrix_X = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

matrix_Y = [[10, 11, 12],
            [13, 14, 15],
            [16, 17, 18]]

print("The multiplication of two given matrices is: ")
print(multiply_numpy_array(matrix_X, matrix_Y))