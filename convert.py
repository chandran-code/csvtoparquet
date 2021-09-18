import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

df = pd.read_csv('D:\\Personal\\BITS\\parquet\\Cancer_Dataset.csv')
print(df)
df.to_parquet('D:\Personal\\BITS\\parquet\\Cancer_Dataset.txt', compression='None')
pd.read_parquet('D:\\Personal\\BITS\\parquet\\Cancer_Dataset.txt')
