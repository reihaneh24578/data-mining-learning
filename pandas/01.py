import pandas as pd
df = pd.read_csv(r"D:\practice machine learning\pandas\01.csv")

print(df[["math", "python", "english"]].mean())
df["average"] = df[["math", "python", "english"]].mean(axis=1)
print(df.nlargest(10, "average"))
print(df[df["average"] < 10])
print(df.head())
print(df.groupby("city")["average"].mean())
print(f"max: \n{df[["math", "python", "english"]].max()}")
print(f"min: \n{df[["math", "python", "english"]].min()}")
mean_python = df["python"].mean()
print(df[df["python"] > mean_python])
