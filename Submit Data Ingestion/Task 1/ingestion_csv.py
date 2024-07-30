import pandas as pd

df = pd.read_csv(".\ingestion-data\dataset\sample.csv", sep=",")
print("Print the first row")
print(df.head(10))