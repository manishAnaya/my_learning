import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('sales_data.csv')

df['Sale_Date'] = pd.to_datetime(df['Sale_Date'])

data = df.groupby(df['Sale_Date'].dt.month_name())['Sales_Amount'].sum()
data.index = pd.CategoricalIndex(data.index, categories=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'], ordered=True)
data = data.sort_index()

plt.figure(figsize=(13, 4))
plt.title('Sales - Monthly Wise')
plt.xlabel('Months')
plt.ylabel('Sale Amount')
plt.plot(data.index, data.values)
plt.show()