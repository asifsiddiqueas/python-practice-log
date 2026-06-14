# python program to transpose a matrix...

import numpy as np

# Defining the matrix variable
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

# Using .T attribute for now and we can use np.transpose() for higher dimension as well
transposed = matrix.T 

print(transposed)