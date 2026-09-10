import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Chocolate Sales.csv')
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
df['Amount'] = df['Amount'].str.replace('[$,]', '', regex=True).astype('float64')

data = df.groupby(
    [df['Date'].dt.year.rename('Year'), df['Date'].dt.month.rename('Month')]
)['Amount'].sum().reset_index()

plt.figure(figsize=(8, 6))
for i, year in enumerate(data['Year'].unique()):
    year_data = data[data['Year'] == year]
    plt.bar(
        [month + (i - 1) * 0.2 for month in year_data['Month']],
        year_data['Amount'],
        width=0.2,
        label=str(year)
    )

plt.title('Monthly Sales Comparison by Year')
plt.xlabel('Month')
plt.ylabel('Sales Amount')
plt.xticks(range(1, 9), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug'])
plt.legend()
plt.show()