import pandas as pd

from bokeh.plotting import figure, show, output_file
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral5
from bokeh.transform import factor_cmap

output_file("01.html")

df = pd.read_csv(r"D:\data mining learning\bokeh\titanic.csv")
df2 = df.groupby("Survived")[["Age", "PassengerId"]].sum().reset_index()
df2["Survived"] = df2["Survived"].astype(str)
print(df2)
data = ColumnDataSource(df2)
Survived = data.data["Survived"].tolist()
p = figure(x_range=Survived)
cm = factor_cmap(field_name="Survived", palette=Spectral5, factors=Survived)
p.vbar(source=data, x="Survived", top="Age", color=cm)
show(p)