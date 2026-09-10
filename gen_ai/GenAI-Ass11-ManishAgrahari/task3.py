import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('sales_data.csv')

data = df.groupby('Product_Category')['Sales_Amount'].sum()

plt.figure(figsize=(8,5))
plt.title('Sales Amount as per Category')
plt.xlabel('Category')
plt.ylabel('Sales Amount')
plt.bar(data.index, data.values)
plt.show()

plt.figure(figsize=(8, 5))
plt.title('Sales Amount as per Category')
plt.xlabel('Sales Amount')
plt.ylabel('Category')
plt.barh(data.index, data.values)
plt.show()