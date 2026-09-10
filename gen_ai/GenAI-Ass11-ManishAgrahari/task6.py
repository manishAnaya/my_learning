import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('sales_data.csv')

plt.figure(figsize=(10, 5))
plt.hist(df['Sales_Amount'], bins=10)

plt.title('Distribution of Sales Amount')
plt.xlabel('Sales Amount')
plt.ylabel('Frequency')

plt.show()