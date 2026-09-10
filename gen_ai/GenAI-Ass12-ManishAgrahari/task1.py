import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('sales_data.csv')

# explore the dataset 
print(df.head())
print(df.shape)
print(df.dtypes)
print(df.isnull().sum())

# Sales_Amount  -> numerical X-axis
# Quantity_Sold -> numerical Y-axis
# Sales_Rep     -> categorical variable for hue

# 1. Creating relational plot using relplot with x and y axis both as numerical
sns.relplot(data=df, x='Sales_Amount', y='Quantity_Sold', kind='line')
plt.show()


# 2. Same relationship using hue as Categorical column
sns.relplot(data=df, x='Sales_Amount', y='Quantity_Sold', hue='Sales_Rep', kind='line')
plt.show()

# 3. Same Plot in scatter kind
sns.relplot(data=df, x='Sales_Amount', y='Quantity_Sold', hue='Sales_Rep', kind='scatter')
plt.show()