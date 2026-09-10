import pandas as pd

## Reading the csv file and storing its data into df as Dataframe
df = pd.read_csv('final_data.csv')

## Printing Shape of df that how many rows and columns its consist of
print(df.shape)

## Printing name of Columns present in df
print(df.columns.to_list())

## Printing First five rows present in df
print(df.head(5))

# Display dataset information including columns, data types, and non-null values
df.info()

## Getting statistical calculation of nymerical columns 
print(df.describe())

## Display frequency of values in Payment Method column
print(df['PaymentMethod'].value_counts())