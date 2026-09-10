import pandas as pd
from sklearn.preprocessing import LabelEncoder, OrdinalEncoder

## Reading the csv file and storing its data into df as Dataframe
df = pd.read_csv('final_data.csv')

## Filling missing values
df['Age'] = df['Age'].fillna(df['Age'].median()).round().astype('int32')
df['City'] = df['City'].fillna(df['City'].mode()[0])
df.columns = ['order_id', 'customer_id', 'order_date', 'product_id', 'quantity', 'discount', 'payment_method', 'status', 'age', 'city', 'signup_date', 'customer_segment', 'product_name', 'category', 'unit_price', 'sales', 'order_value']
## Fixing incorrect Dtypes
numerical_cols = ['order_id', 'customer_id', 'product_id', 'quantity', 'discount', 'age', 'unit_price', 'sales', 'order_value']
categorical_cols = ['payment_method', 'status', 'city', 'customer_segment', 'product_name', 'category']
date_cols = ['order_date', 'signup_date']
for col in numerical_cols:
    df[col] = df[col].astype('int32')
for col in categorical_cols:
    df[col] = df[col].astype('category')
for col in date_cols:
    df[col] = pd.to_datetime(df[col], errors='coerce')

## TASK 7

## For converting categorical columns into numerical, Getting value count to see which encoder can be used for which column
# for col in categorical_cols:
#     print(df[col].value_counts())

## Found customer_segment as Ordinal and rest as Label
oe = OrdinalEncoder(categories=[['New', 'Regular', 'VIP']])
df[['customer_segment']] = oe.fit_transform(df[['customer_segment']])

le = LabelEncoder()
df['payment_method'] = le.fit_transform(df['payment_method'])
df['status'] = le.fit_transform(df['status'])
df['city'] = le.fit_transform(df['city'])
df['product_name'] = le.fit_transform(df['product_name'])
df['category'] = le.fit_transform(df['category'])

print(df.head())

# Feature extracting
df['sales_per_unit'] = df['sales'] / df['quantity']

## Separating Features and Target

X = df.drop(columns=['sales'])
Y = df['sales']

print("X Shape:", X.shape)
print("y Shape:", Y.shape)

print(X.head())
print(Y.head())