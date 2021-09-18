import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

df = pd.read_csv('Cancer_Dataset.csv')
print(df)
df.to_parquet('Cancer_Dataset.txt', compression='None')
pd.read_parquet('Cancer_Dataset.txt')
