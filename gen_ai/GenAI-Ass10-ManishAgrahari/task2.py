import pandas as pd

marks = [78, 85, 90, 66, 72]

series = pd.Series(marks)

print("By Adding")
print(series + 5)

print("By Subtracting")
print(series - 2)

print("By Multiplying")
print(series * 1.05)

print("By Dividing")
print(series / 2)