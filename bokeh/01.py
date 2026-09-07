from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from bokeh.models import HoverTool
import pandas as pd
output_file("salam.html")

df = pd.read_csv(r"D:\data mining learning\matplotlib\01.csv").sample(100)
print(df.head())

data = ColumnDataSource(df)

p = figure()
p.line(source=data, x="Age", y="PassengerId", color="red",legend_label="hello")
p.circle(source=data, x="Age", y="PassengerId", size=10, legend_label="reihaneh")
p.scatter(source=data, x= "Age", y="PassengerId", legend_label="sharifi")
p.vbar(source=data, x="Age", top="PassengerId", legend_label="welcome")
p.legend.click_policy= "hide"

hover = HoverTool()
hover.tooltips = [("Age", "@Age"), ("PassengerId", "@PassengerId")]
p.add_tools(hover)
show(p)


