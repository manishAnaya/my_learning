import pandas as pd

## Reading the csv file and storing its data into df as Dataframe
df = pd.read_csv('final_data.csv')

## Dataset Shape
print(df.shape)

## Checking some structure and values
print(df.head())
df.info()

## Columns Datatypes
print(df.dtypes)

## Checking missing values per columns
print(df.isna().sum())

## Checking duplicates
print(df.duplicated().sum())

