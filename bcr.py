import bar_chart_race as bcr
import pandas as pd

source = pd.read_json("https://cea.nic.in/api/installed_capacity.php")

df = source[["Region", "Month","Total"]]

df = df.pivot(index = "Month", columns= "Region", values = "Total")

df = df.dropna()

#sort by time please

print(df)
# bcr.bar_chart_race(
#     df = df,
#     filename = "trial.mp4",
# )