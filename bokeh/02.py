import pandas as pd
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, show, output_file

output_file("titanic.html")
df = pd.read_csv(r"D:\data mining learning\matplotlib\01.csv")
data = ColumnDataSource(df)

p = figure()
p.line(source=data, x="Fare", y="Pclass", color="red", legend_label="type of price")
p.scatter(source=data, x="Survived", y="SibSp", legend_label="number")
p.vbar(source=data, x="sex", top="Survived")
p.legend.click_policy = 'mute'
show(p)