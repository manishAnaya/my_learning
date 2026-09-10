import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('sales_data.csv')

# Converting Sale_Date to datetime
df['Sale_Date'] = pd.to_datetime(df['Sale_Date'])

# explore the dataset 
print(df.head())
print(df.shape)
print(df.dtypes)
print(df.isnull().sum())

# Sale_Date  -> numerical X-axis
# Sales_Amount -> numerical Y-axis
# Region -> column variable for col

# 1. Creating line plot using sns.lineplot()
sns.lineplot(data=df, x='Sale_Date', y='Sales_Amount')
plt.show()

# 2. Same relationship using scatter plot
sns.lineplot(data=df, x='Sale_Date', y='Sales_Amount', marker='o')
plt.show()

#3. Splitting the plot based on Region 
sns.relplot(data=df, x='Sale_Date', y='Sales_Amount', col='Region', kind='line', col_wrap=2)
plt.show()