import bar_chart_race as bcr
import pandas as pd
from datetime import datetime


source = pd.read_json("https://cea.nic.in/api/installed_capacity.php")

source = source[["Region","Month","Total"]]
source = source.drop_duplicates()

source = source.pivot(index = "Month",columns= "Region", values = "Total")

source = source.dropna()

sorted_source = pd.DataFrame(columns=["Northern","Eastern","Western","Southern","North Eastern"])

for index,row in source.iterrows():
    new_index = datetime.strptime(index, "%b-%Y")
    sorted_source.loc[new_index] = [row["Northern"],row["Eastern"],row["Western"],row["Southern"],row["North Eastern"]]

sorted_source = sorted_source.sort_index()

df = pd.DataFrame(columns=["Northern","Eastern","Western","Southern","North Eastern"])

for index,row in sorted_source.iterrows():
    new_index = datetime.strftime(index, "%b-%Y")
    df.loc[new_index] = [row["Northern"],row["Eastern"],row["Western"],row["Southern"],row["North Eastern"]]

bcr.bar_chart_race(
    df = df,
    filename = "trial.mp4",
    title = "Total Capacity by Regional Grid"
)