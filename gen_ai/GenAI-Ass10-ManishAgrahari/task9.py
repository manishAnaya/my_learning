import pandas as pd
import matplotlib.pyplot as plt

sales = {
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri"],
    "Revenue": [1200, 1500, 900, 2000, 1800]
}

df = pd.DataFrame(sales)

print(f"Total Revenue: {df['Revenue'].sum()}")
print(f"Avg. Daily Revenue: {df['Revenue'].mean()}")

highest_revenue = df.loc[df['Revenue'].idxmax(), "Day"]
print(f"Day with highest Revenue: {highest_revenue}")
print(f"Days with Revenue greater than Avg: \n{df[df['Revenue'] > df['Revenue'].mean()]}")

df.plot(x="Day", y="Revenue")
plt.show()
