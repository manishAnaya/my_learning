import pandas as pd

marks = [78, 85, 90, 66, 72]

series = pd.Series(marks)

maximum_marks = series.max()
minimum_marks = series.min()
sum_marks = series.sum()
mean_marks = series.mean()

print(f"Max Marks: {maximum_marks}\nMin Marks: {minimum_marks}\nSum of Marks: {sum_marks}\nAverage Mark: {mean_marks}")

passed = series.apply(lambda x: x >= 70 )
print(f"Number of Student passed: {passed.sum()}")