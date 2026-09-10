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

# Sales_Amount  -> numerical X-axis 
# Quantity_Sold -> numerical Y-axis
# Using two numerical columns for bivariate distribution analysis

# 1.Bivariate Histogram
sns.histplot(data=df, x='Sales_Amount', y='Quantity_Sold')
plt.show()

# 2.Bivariate KDE
sns.kdeplot(data=df, x='Sales_Amount', y='Quantity_Sold')
plt.show()