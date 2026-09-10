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
# Product_Category -> categorical column
# Region -> categorical column
# Sales_Rep -> categorical column

# 1. FacetGrid with 2 numerical columns x as Sales_Amount and y as Quantity_Sold with col as Product_Category to show Grid
sns.relplot(data=df, x='Sales_Amount', y='Quantity_Sold', col='Product_Category', hue='Product_Category', col_wrap=2)
plt.show()

# 2.Multiplot using relplot, displot and catplot

# Relational multi-plot
sns.relplot(data=df, x='Sales_Amount', y='Quantity_Sold', col='Region', col_wrap=2)
plt.show()

# Distribution multi-plot
sns.displot(data=df, x='Sales_Amount', col='Sales_Rep', col_wrap=2)
plt.show()

# Categorical multi-plot
sns.catplot(data=df, x='Product_Category', y='Sales_Amount', col='Region', col_wrap=2, kind='bar')
plt.show()
























# # 1.
# tips = sns.load_dataset('tips')
# sns.relplot(data=tips, x='total_bill', y='tip', col='time', hue='sex')
# plt.show()


# 2.
# df = pd.read_csv('sales_data.csv')
# sns.relplot(data=df, x='Sales_Amount', y='Quantity_Sold', hue='Sales_Rep', col='Region', kind='scatter', col_wrap=2)
# plt.show()

# sns.catplot(data=df, x='Product_Category', y='Sales_Amount', col='Region', kind='bar', col_wrap=2)
# plt.show()

# sns.displot(data=df, x='Sales_Amount', col='Sales_Rep', kind='hist', col_wrap=2)
# plt.show()