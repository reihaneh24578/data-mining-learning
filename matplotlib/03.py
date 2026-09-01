import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r"D:\data mining learning\matplotlib\03_movies.csv")
print(df.head())
plt.figure()
df.plot.scatter(x="Rating", y="Revenue_Million")
df.plot.scatter(x="Votes", y="Rating")
plt.figure()
df["Rating"].hist()
plt.bar(df["Title"], df["Runtime_Minutes"])
plt.figure()
df.plot.line(x="Rating", y="Year")
plt.show()