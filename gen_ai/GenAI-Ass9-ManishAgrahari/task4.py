import numpy as np

data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

row_by_sum = np.sum(data, axis = 1)
col_by_sum = np.sum(data, axis = 0)
min_value = np.min(data)
max_value = np.max(data)
overall_mean = np.mean(data)

print("Row-wise Sum:", row_by_sum)
print("Column-wise Sum:", col_by_sum)
print("Minimum:", min_value)
print("Maximum:", max_value)
print("Overall Mean:", overall_mean)