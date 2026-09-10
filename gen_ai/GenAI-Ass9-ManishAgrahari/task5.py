import numpy as np

marks = np.array([78, 85, 90, 66, 72, 88, 95, 60])

mean = np.mean(marks)
median = np.median(marks)
variance = np.var(marks)
std_dev = np.std(marks)
min_marks = np.min(marks)
max_marks = np.max(marks)
data_range = max_marks - min_marks

print("Mean:", mean)
print("Median:", median)
print("Variance:", variance)
print("Standard Deviation:", std_dev)
print("Minimum:", min_marks)
print("Maximum:", max_marks)
print("Range:", data_range)
