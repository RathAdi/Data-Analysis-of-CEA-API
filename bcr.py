import bar_chart_race as bcr
import pandas as pd

source = pd.read_json("https://cea.nic.in/api/installed_capacity.php")

df = source[["Region", "Month","Total"]]

hold = df.pivot(index = "Month", columns= "Region", values = "Total")

hold.drop(["Oct-2023"])

bcr.bar_chart_race(
    df = hold,
    filename = "trial.mp4",
)