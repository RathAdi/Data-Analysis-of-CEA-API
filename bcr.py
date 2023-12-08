import bar_chart_race as bcr
import pandas as pd

source = pd.read_json("https://cea.nic.in/api/installed_capacity.php")

df = source[["Region", "Month","Total"]]

# hold = pd.DataFrame(columns=["Date", "Northern", "Eastern", "Western", "Southern", "North Eastern"])

hold = df.pivot(index = "Month", columns= "Region", values = "Total")

print(hold)

# bcr.bar_chart_race(
#     df = df,
#     filename = "trial.mp4",
# )