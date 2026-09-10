import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

## Reading the csv file and storing its data into df as Dataframe
df = pd.read_csv('final_data.csv')
print(df.head())

## Histogram with KDE enabled to show Plot distribution of numerical columns 
sns.histplot(data=df, x='Sales', kde=True)
plt.show()

## Count Plot for categorical columns
sns.countplot(data=df, x='CustomerSegment')
plt.show()

sns.countplot(data=df, x='PaymentMethod') 
plt.show()

## Boxplot to show Plot Spreads and outliers
sns.boxplot(data=df, x='Sales')
plt.show()
