from openpyxl import Workbook
import pandas as pd

myWorkbook = Workbook()

currWs = myWorkbook.active

currWs["A1"] = "First Name"
currWs["B1"] = "Last Name"
currWs["C1"] = "Favorite Food"

currWs["A2"] = "Luke"
currWs["B2"] = "Skywalker"
currWs["C2"] = "Nausage"

currWs["A3"] = "Leia"
currWs["B3"] = "Organa"
currWs["C3"] = "Ruica"

currWs["A4"] = "Han"
currWs["B4"] = "Solo"
currWs["C4"] = "Chytuck"

currWs["A5"] = "Ben"
currWs["B5"] = "Solo"
currWs["C5"] = "Spaghetti"

myWorkbook.save(filename="test.xlsx")
myWorkbook.close()

df = pd.read_excel("test.xlsx", names=["First", "Last", "Food"])

df = df.sort_values(["Last", "First"], ascending=[False, True])

print(df)

