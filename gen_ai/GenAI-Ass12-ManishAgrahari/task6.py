import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('sales_data.csv')

# explore the dataset 
print(df.head())
print(df.shape)
print(df.dtypes)
print(df.isnull().sum())


# 1.Bar plot with Categorical column (Product_Category) and numerical column (Sales_Amount)
sns.barplot(data=df, x='Product_Category', y='Sales_Amount')
plt.show()

# 2.Box plot with Categorical column (Sales_Rep) and numerical column (Sales_Amount)
sns.boxplot(data=df, x='Sales_Rep', y='Sales_Amount')
plt.show()

# 3.Violin plot with Categorical column (Sales_Rep) and numerical column (Sales_Amount)
sns.violinplot(data=df, x='Sales_Rep', y='Sales_Amount')
plt.show()

# 4.Count plot with Categorical column (Product_Category) to show the number of records in each category
sns.countplot(data=df, x='Product_Category')
plt.show()