import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('sales_data.csv')

# explore the dataset 
print(df.head())
print(df.shape)
print(df.dtypes)
print(df.isnull().sum())

# Sales_Amount -> numerical X-axis 
# Quantity_Sold -> numerical Y-axis 

# 1. Regression Plot using 2 numerical Columns
# Using first 50 rows to make the regression plot easier to understand
sns.regplot(data=df.head(50), x='Sales_Amount', y='Quantity_Sold')
plt.show()

# 2. Implot with hue as Categorical column (Sales_Rep)
sns.lmplot(data=df.head(50), x='Sales_Amount', y='Quantity_Sold', hue='Sales_Rep')
plt.show()