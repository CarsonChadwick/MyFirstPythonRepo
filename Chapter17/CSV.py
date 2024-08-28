import pandas as pd

dfTeams = pd.read_csv("Infos.csv", index_col ="Team")

dfNew = dfTeams.iloc[1][0]
dfOld = dfTeams.iloc[1]
print(dfNew)
print(dfOld)
