import bar_chart_race as bcr
import pandas as pd
from datetime import datetime

source = pd.read_json("https://cea.nic.in/api/installed_capacity.php")

source = source[["Region","Month","Total"]]

source = source.pivot(index = "Month",columns= "Region", values = "Total")
source = source.drop_duplicates()

source = source.dropna()

df = pd.DataFrame(columns=["Northern","Eastern","Western","Southern","North Eastern"])

for index,row in source.iterrows():
    new_index = datetime.strptime(index, "%b-%Y")
    df.loc[new_index] = [row["Northern"],row["Eastern"],row["Western"],row["Southern"],row["North Eastern"]]

df = df.sort_index()

bcr.bar_chart_race(
    df = df,
    filename = "trial.mp4"
)