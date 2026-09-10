import pandas as pd

## Reading the csv file and storing its data into df as Dataframe
df = pd.read_csv('final_data.csv')

## Checking for missing values
print(df.isna().sum()) 

## Found Age and City Columns have some missing values
## Filling missing values
df['Age'] = df['Age'].fillna(df['Age'].median()).round().astype('int32')
df['City'] = df['City'].fillna(df['City'].mode()[0])

## Checking the starus now
print(df.isna().sum())

## checking for duplicates
print(df.duplicated().sum())
## Found 0

print(df.columns.to_list())
## Renaming columns to lower and snake_case
df.columns = ['order_id', 'customer_id', 'order_date', 'product_id', 'quantity', 'discount', 'payment_method', 'status', 'age', 'city', 'signup_date', 'customer_segment', 'product_name', 'category', 'unit_price', 'sales', 'order_value']

print(df.head())

## Fixing incorrect Dtypes
numerical_cols = ['order_id', 'customer_id', 'product_id', 'quantity', 'discount', 'age', 'unit_price', 'sales', 'order_value']
categorical_cols = ['payment_method', 'status', 'city', 'customer_segment', 'product_name', 'category']
date_cols = ['order_date', 'signup_date']

## As all numerical columns dont have any decimal values, So all is converted into int32
for col in numerical_cols:
    df[col] = df[col].astype('int32')

for col in categorical_cols:
    df[col] = df[col].astype('category')

for col in date_cols:
    df[col] = pd.to_datetime(df[col], errors='coerce')

df.info()
