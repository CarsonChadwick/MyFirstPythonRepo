from openpyxl import Workbook

myWorkbook = Workbook()
currSheet = myWorkbook.active
currSheet["A1"] = "First Name"
currSheet["B1"] = "Last Name"
currSheet["C1"] = "Favorite Food"
currSheet["D1"] = "Calories"

currSheet["A2"] = "Yogi"
currSheet["B2"] = "Bear"
currSheet["C2"] = "Honey"
currSheet["D2"] = 64

myWorkbook.save(filename="firstexcel.xlsx")

myWorkbook.close()