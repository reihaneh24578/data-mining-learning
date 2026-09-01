import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"D:\data mining learning\matplotlib\01_student_scores.csv")
print(df.head())
plt.bar(df["Score"], df["Name"])
plt.figure()
df["Score"].hist()
df.sort_values(["Score"], inplace=True)
df.plot.line(x="Score", y="Student_ID")
plt.show()