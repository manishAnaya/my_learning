import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('sales_data.csv')

plt.figure(figsize=(6, 6))

category_sale = df.groupby('Product_Category')['Sales_Amount'].sum()
plt.pie(category_sale, labels=category_sale.index, autopct='%1.1f%%')

plt.title('Sales Distribution by Product Category')
plt.legend()
plt.show()