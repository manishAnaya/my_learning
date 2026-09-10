import numpy as np

A = np.array([10, 20, 30, 40])
B = np.array([1, 2, 3, 4])

addition = A + B
subtraction = A - B
multiplication = A * B
division = A / B
power = A ** B
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
print("Power:", power)

add = np.add(A, B)
print(add)
subtract = np.subtract(A, B)
print(subtract)