import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

## Reading the csv file and storing its data into df as Dataframe
df = pd.read_csv('final_data.csv')

## Customer Segment Analysis wrt Sales
print(df.groupby('CustomerSegment')['Sales'].mean().sort_values(ascending=False))
# Insight:
# Regular customers have the highest average sales (70.15), followed closely by New customers (70.13).
# VIP customers have the lowest average sales (68.56).
# The difference between them is small.

## Customer Segment Analysis wrt Discount
print(df.groupby('CustomerSegment')['Discount'].mean().sort_values(ascending=False))
# Insight:
# VIP customers have the highest discount (7.58), followed closely by Regular customers (7.50).
# VIP customers have the lowest average sales (7.43).
# The difference between them is small of about 0.07.

## Payment Method Analysis
print(df['PaymentMethod'].value_counts())
# Insight:
# Gateway is the most frequently used payment method with 23,894 transactions.
# Cash is the least frequently used payment method with 4,923 transactions.

## Category Analysis
print(df.groupby('Category')['Sales'].sum().sort_values(ascending=False))
# Insight:
# Electronics generates the highest total sales with approximately 1.75 million.
# Stationery generates the lowest total sales with approximately 67,218.

## Negative Sales Analysis
negative_sales = df[df['Sales'] < 0]
print("Number of negative sales:", len(negative_sales))
print(negative_sales['Status'].value_counts())
# Insight:
# Only 19 transactions have negative sales values.
# 18 of these transactions have a completed status and 1 has a cancelled status.
# negative sales should be investigated

## Sales Analysis for outliers using BoxPlot
sns.boxplot(data=df, x='Sales')
plt.show()
# Insight:
# The Sales boxplot shows several potential outliers on both the lower and upper sides with some values reaching around 1300.
# A few negative Sales values also appear as lower-side outliers.
# These values should be investigated to determine whether they are valid

## Average Sales by Category and Customer Segment Analysis
sns.barplot(data=df, x='Category', y='Sales', hue='CustomerSegment', estimator='mean')
plt.xticks(rotation=45)
plt.title('Average Sales by Category and Customer Segment')
plt.show()
# Insight:
# Average Sales varies considerably across product categories.
# Home Office has the highest average Sales, while Stationery has the lowest.
# The best-performing Customer Segment also varies across categories,
# indicating that customer segment performance depends on the product category.