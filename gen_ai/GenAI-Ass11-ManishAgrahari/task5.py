import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('sales_data.csv')

sales_data = df.groupby(['Sales_Rep', 'Product_Category'])['Sales_Amount'].sum().reset_index()
categories = sales_data['Product_Category'].unique()
sales_person = sales_data['Sales_Rep'].unique()
bottom = np.zeros(len(sales_person))
plt.figure(figsize=(10, 8))

for category in categories:
    data = sales_data[sales_data['Product_Category'] == category]
    print(data)
    print(type(data))
    plt.bar(
        sales_person,
        data['Sales_Amount'],
        bottom=bottom,
        label=category
    )
    bottom += data['Sales_Amount'].values

plt.title('Sales by Sales Representative and Product Category')
plt.xlabel('Sales Representative')
plt.ylabel('Sales Amount')
plt.legend()
plt.show()