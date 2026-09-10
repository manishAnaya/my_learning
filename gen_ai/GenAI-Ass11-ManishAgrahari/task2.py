import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('sales_data.csv')

sales = df['Sales_Amount']
quantity = df['Quantity_Sold']
plt.xlabel('Quantity Sold')
plt.ylabel('Sales Amount')
plt.title('Quantity Sold vs Sales Amount')
plt.scatter(quantity, sales)
plt.show()