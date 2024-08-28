import pandas as pd

dfCandy = pd.read_csv("inClass.csv", index_col="Description")

print(dfCandy.loc["Snickers"])