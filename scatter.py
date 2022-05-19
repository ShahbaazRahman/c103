import plotly.express as px
import csv
import pandas as pd
df = pd.read_csv("date6.csv")

fig = px.scatter(df,x = "date", y = "cases", color = "country")
fig.show()