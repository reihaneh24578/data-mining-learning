import pandas as pd
df = pd.read_csv(r"D:\practice machine learning\pandas\02.csv")
df["income"] = df["quantity"] * df["price"]
print(df.head())
print(df["income"].sum())
print(df.groupby("product")["quantity"].sum().idxmax())
print(df.groupby("product")["income"].sum().idxmax())
print(df.groupby("city")["income"].sum())
print(df.groupby("category")["income"].sum())