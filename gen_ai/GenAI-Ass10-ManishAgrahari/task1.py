import pandas as pd

marks = [78, 85, 90, 66, 72]

series = pd.Series(marks)

print(f"Series:\n{series}")
print(f"Series Index: {series.index}")
print(f"Data Type: {series.dtypes}")
print(f"First Element: {series[0]}")
print(f'Last two Elements:\n{series[-2:]}')