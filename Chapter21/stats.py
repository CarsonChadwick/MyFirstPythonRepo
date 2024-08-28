import pandas as pd
df = pd.read_excel("describe.xlsx")

df = df.sort_values(["Exam 1"], ascending=[False])
df.to_excel("newDescribe.xlsx")
#print(df.head(2))
#print(df.tail(2))
#print(df.sample(3))
#print(df.info())
#print(df.corr())
#print(df.describe())