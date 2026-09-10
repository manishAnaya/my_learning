import numpy as np

sales = np.array([1200, 1500, 900, 2000, 1800, 1700, 1600])

total_weekly_sales = np.sum(sales)
avg_daily_sales = np.mean(sales)
highest_sales = np.max(sales)
lowest_sales = np.min(sales)
std_dev_sales = np.std(sales)
days = np.arange(1, 8)
above_average_days = days[sales > avg_daily_sales]

print("Total Weekly Sales:", total_weekly_sales)
print("Average Daily Sales:", avg_daily_sales)
print("Highest Sales:", highest_sales)
print("Lowest Sales:", lowest_sales)
print("Standard Deviation:", std_dev_sales)
print("Days Above Average:", above_average_days )

