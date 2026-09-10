import pandas as pd

## Reading the json file and storing its data into df as Dataframe
df = pd.read_json('products.json')

print(df.head())