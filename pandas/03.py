import pandas as pd
import numpy as np
df = pd.read_csv(r"D:\practice machine learning\pandas\03.csv")
print(df.info())
print(df.describe())
print(df.isnull().sum())
df = df.drop_duplicates()
print(df)
print(df[(df["age"] > 80) | (df["age"] < 0)])
df.loc[(df["age"] > 80) | (df["age"] < 0), "age"] = np.nan
df["age"] = df["age"].fillna(df["age"].median())
print(df)
df["salary"] = df["salary"].fillna(df["salary"].median())
print(df)
df["city"] = df["city"].fillna(df["city"].mode()[0])
print(df)
print(df["city"].mode())