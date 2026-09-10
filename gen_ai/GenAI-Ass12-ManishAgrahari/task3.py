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

# Sales_Amount  -> numerical X-axis for univariate distribution Analysis

# 1.Plotting histogram
sns.histplot(data=df, x='Sales_Amount')
plt.show()

# 2.Plotting KDE plot
sns.kdeplot(data=df, x='Sales_Amount')
plt.show()

# 3.Plotting Rug plot
sns.rugplot(data=df, x='Sales_Amount')
plt.show()

# 4.Plotting combination of hist and kde
sns.histplot(data=df, x='Sales_Amount', kde=True)
plt.show()

