import numpy as np

one_d_array = np.arange(1, 11)

two_d_array = np.arange(1, 10).reshape(3, 3)

list = [10, 20, 30, 40, 50]
array = np.array(list)

print("1D Array:", one_d_array)
print("2D Array:")
print(two_d_array)
print("Array from list:", array)

# Shape
print("\nShapes:")
print(one_d_array.shape)
print(two_d_array.shape)
print(array.shape)

# Data types
print("\nData Types:")
print(one_d_array.dtype)
print(two_d_array.dtype)
print(array.dtype)