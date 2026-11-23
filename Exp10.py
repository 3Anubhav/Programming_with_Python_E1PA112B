import numpy as np

# Creating 1-D Array
arr1 = np.array([10, 20, 30, 40])
print("1-D Array:", arr1)

# Creating 2-D Array
arr2 = np.array([[1, 2], [3, 4]])
print("\n2-D Array:\n", arr2)

# Inspecting Array
print("\nDimensions:", arr2.ndim)
print("Shape:", arr2.shape)
print("Data Type:", arr2.dtype)

# Array Arithmetic
print("\nAddition:", arr1 + 5)
print("Subtraction:", arr1 - 5)
print("Multiplication:", arr1 * 2)
print("Division:", arr1 / 2)

# Matrix Addition
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("\nMatrix Addition:\n", A + B)

# Matrix Transpose
print("\nMatrix Transpose:\n", A.T)