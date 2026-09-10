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

# Sales_Rep -> categorical column
# Sale_Date -> used as index in the pivot table
# Sales_Amount -> values used in the pivot table

# 1.Creating pair plot with df 
sns.pairplot(data=df)
plt.show()

# Creating pivot table for heatmap
data = df.pivot_table(columns='Sales_Rep', index='Sale_Date', values='Sales_Amount', aggfunc='sum')

# Convert datetime to normal date format
data.index = data.index.strftime('%Y-%m-%d')

# 2. Heatmap
sns.heatmap(data=data.head(30), annot=True, cmap='viridis', linewidths=0.5)
plt.show()