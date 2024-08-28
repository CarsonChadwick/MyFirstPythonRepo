from openpyxl import Workbook

myWorkbook = Workbook()
currSheet = myWorkbook.active

currSheet["A1"] = "First Name"
currSheet["B1"] = "Last Name"
currSheet["C1"] = "Favorite Food"

currSheet["A2"] = "Carmen"
currSheet["B2"] = "Sandiego"
currSheet["C2"] = "Fish"

currSheet.column_dimentions["A"].width = 20
currSheet.column_dimentions["B"].width = 20
currSheet.column_dimentions["C"].width = 20

myWorkbook.save(filename="firstexcel.xlsx")
myWorkbook.close
