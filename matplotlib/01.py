import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv(r"D:\practice machine learning\matplotlib\titanic.csv")
print(df.head())

# df["Age"].hist(bins=30)
# df.sort_values(by="Age").plot.line(x="Age", y="Fare")
# df.plot.hexbin(x="Age", y="Fare", gridsize=20, cmap="Blues")
# df.plot.scatter(x="Age", y="Fare")
df.boxplot()
df.hist()
plt.show()