import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

## Reading the csv file and storing its data into df as Dataframe
df = pd.read_csv('final_data.csv')
print(df.head())

## Scatter Plot -> Relationship between Age and Sales
sns.scatterplot(data=df, x='Age', y='Sales')
plt.show()

## Bar Plot -> Average Sales for each Customer Segment
sns.barplot(data=df, x='CustomerSegment', y='Sales')
plt.show()

## Bar Plot -> Average Sales for each Payment Method
sns.barplot(data=df, x='PaymentMethod', y='Sales')
plt.show()

## Box Plot -> Distribution of Sales across Customer Segments
sns.boxplot(data=df, x='CustomerSegment', y='Sales')
plt.show()

## Grouped Count Plot -> Payment Method vs Customer Segment
sns.countplot(data=df, x='PaymentMethod', hue='CustomerSegment')
plt.show()

## Histogram with Bivariate Analysis so see the realtion between Sales as per CustomerSegment
sns.histplot(data=df, x='CustomerSegment', y='Sales')
plt.show()

## Correlation Heatmap -> Relationship between numerical variables
numerical_cols = [
    'Quantity',
    'Discount',
    'Age',
    'UnitPrice',
    'Sales',
    'OrderValue'
]

correlation = df[numerical_cols].corr()
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.show()