import bar_chart_race as bcr
import pandas as pd
from datetime import datetime

#add renewables capacities too

def make_bcr(field="Total"):
    source = pd.read_json("https://cea.nic.in/api/installed_capacity.php")

    source = source[["Region","Month",field]]
    source = source.drop_duplicates()
    
    source = source.pivot(index = "Month",columns= "Region", values = field)

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
        filename = f"{field}.mp4",
        title = f"{field} Generation Capacity by Grid Regions"
    )

for i in ["Total", "Coal","Hydro","Nuclear","Gas","Diesel"]:
    make_bcr(i)